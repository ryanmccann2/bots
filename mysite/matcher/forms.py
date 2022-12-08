from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(forms.ModelForm):
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
            'years_of_experience',
            'education',
            # Additional fields for recruiter profiles:
            'company_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Show only the fields relevant to the selected profile type
        profile_type = self.initial.get('profile_type', User.PROFILE_TYPE_CANDIDATE)
        if profile_type == User.PROFILE_TYPE_CANDIDATE:
            self.fields.update([
                ('profile_type', self.fields['profile_type']),
                ('first_name', self.fields['first_name']),
                ('last_name', self.fields['last_name']),
                ('zip_code', self.fields['zip_code']),
                ('username', self.fields['username']),
                ('password', self.fields['password']),
                ('profile_bio', self.fields['profile_bio']),
                ('skills', self.fields['skills']),
                ('years_of_experience', self.fields['years_of_experience']),
                ('education', self.fields['education']),
            ])
        elif profile_type == user.PROFILE_TYPE_RECRUITER:
            self.fields.update([
                ('profile_type', self.fields['profile_type']),
                ('first_name', self.fields['first_name']),
                ('last_name', self.fields['last_name']),
                ('company_name', self.fields['company_name']),
                ('zip_code', self.fields['zip_code']),
                ('username', self.fields['username']),
                ('password', self.fields['password']),
            ])
            
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class CandidateOrRecruiterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'profile_type'
        ]
