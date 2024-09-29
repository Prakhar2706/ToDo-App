import re
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken. Please use a different username.")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        
        # Check if password starts with a number
        if password[0].isdigit():
            raise forms.ValidationError("Password cannot start with a number.")

        # Check for at least one lowercase letter, uppercase letter, number, and special character
        if (not re.search(r'[a-z]', password) or
            not re.search(r'[A-Z]', password) or
            not re.search(r'\d', password) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            raise forms.ValidationError(
                "Password must contain at least one lowercase letter, one uppercase letter, one number, and one special character."
            )

        # Check password length
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
