from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .UserCreationForm import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.core.exceptions import ValidationError
from django import forms
import re
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

# Register view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Save first_name and last_name in the User model
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()

            # Create a profile linked to the user
            profile, created = Profile.objects.get_or_create(user=user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()

            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'tasks/register.html', context)


@login_required
def edit_profile(request):
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':
        # Update first name and last name for both Profile and User
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        profile.first_name = user.first_name
        profile.last_name = user.last_name

        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES['profile_image']

        # Check if clear_image button was pressed
        if 'clear_image' in request.POST:
            profile.profile_image.delete()  # Delete the image if needed
            profile.profile_image = None

        # Save both user and profile
        user.save()
        profile.save()
        
        return redirect('edit_profile')

    return render(request, 'tasks/edit_profile.html', {'profile': profile, 'user': user})


@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('complete', 'due_date', 'id')  
    form = TaskForm()

    # Filtering logic
    filter_type = request.GET.get('filter')
    due_date = request.GET.get('due_date')
    search_query = request.GET.get('search')

    if filter_type == 'priority':
        tasks = tasks.filter(priority=True)
    elif due_date:
        tasks = tasks.filter(due_date__date=due_date)

    if search_query:
        tasks = tasks.filter(title__icontains=search_query) | tasks.filter(description__icontains=search_query)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)



@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk, user=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)

@login_required(login_url='login')
def completeTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('/')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

class CustomPasswordResetForm(auth_views.PasswordResetConfirmView):
    def form_valid(self, form):
        password1 = form.cleaned_data.get("new_password1")
        password2 = form.cleaned_data.get("new_password2")

        # Ensure passwords match
        if password1 != password2:
            form.add_error('new_password2', "Passwords do not match.")
            return self.form_invalid(form)

        # Validate the complexity of the password
        try:
            self.custom_password_validation(password1)
        except ValidationError as e:
            form.add_error('new_password1', e.message)
            return self.form_invalid(form)

        return super().form_valid(form)

    def custom_password_validation(self, password):
        # Custom password rules
        if password[0].isdigit():
            raise ValidationError("Password cannot start with a number.")
        
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        
        if not (re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'\d', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            raise ValidationError("Password must contain at least one lowercase letter, one uppercase letter, one number, and one special character.")