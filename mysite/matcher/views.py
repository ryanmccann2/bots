from django.views import View
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from .forms import UserSignupForm, UserLoginForm
from .models import User

def home(request):
    return render(request, 'matcher/home.html')

class UserSignupView(View):
    def get(self, request):
        form = UserSignupForm()
        return render(request, 'matcher/signup.html', {'form': form})

    def post(self, request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            # Generate a unique identifier for the user
            identifier = get_random_string(length=100)
            while User.objects.filter(identifier=identifier).exists():
                identifier = get_random_string(length=100)

            # Create the user profile
            profile = form.save(commit=False)
            profile.identifier = identifier
            profile.save()

            messages.success(request, 'Your profile has been created successfully!')
            return redirect('user_profile', identifier=identifier)

        return render(request, 'matcher/signup.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'matcher/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have been logged in successfully!')
                return redirect('user_profile', identifier=user.identifier)

            messages.error(request, 'Invalid username or password')

        return render(request, 'matcher/login.html', {'form': form})