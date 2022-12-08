from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'profile_type',
            'first_name',
            'last_name',
            'zip_code',
            'username',
            'password',
            # Additional fields for candidate profiles:
            'profile_bio',
            'skills',
            'github_username',
            'years_of_experience',
            'education',
            # Additional fields for recruiter profiles:
            'company_name',
            'company_website',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Show only the fields relevant to the selected profile type
        profile_type = self.initial.get('profile_type', User.PROFILE_TYPE_CANDIDATE)
        if profile_type == User.PROFILE_TYPE_CANDIDATE:
            self.fields = [
                'profile_type',
                'first_name',
                'last_name',
                'zip_code',
                'username',
                'password',
                'profile_bio',
                'skills',
                'github_username',
                'years_of_experience',
                'education',
            ]
        elif profile_type == user.PROFILE_TYPE_RECRUITER:
            self.fields = [
                'profile_type',
                'first_name',
                'last_name',
                'company_name',
                'zip_code',
                'username',
                'password',
            ]
            
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
