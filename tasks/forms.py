from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...', 'style': 'width: 100%;'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'style': 'width: 100%;', 'placeholder': 'Description...'}))
    due_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'style': 'width: 100%;', 'placeholder': 'Due date...'}))
    priority = forms.BooleanField(required=False)
    file_attachment = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'style': 'width: 100%;'}))

    class Meta:
        model = Task
        exclude = ['user', 'created']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_image']
    
    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        # If no image is uploaded, return None to keep the existing image
        if not profile_image:  # If no image is uploaded
            return None  # Return None to keep the existing image
        # Optionally, you can add validation for the image file type
        if not profile_image.name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            raise forms.ValidationError("Only image files are allowed (PNG, JPG, JPEG, GIF).")
        return profile_image