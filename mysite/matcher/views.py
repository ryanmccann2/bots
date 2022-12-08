from django.views import View
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from .forms import UserSignupForm, UserLoginForm, CandidateOrRecruiterForm
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
            return redirect('candidate_or_recruiter')
        return render(request, 'matcher/signup.html', {'form': form})


class UserCLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'matcher/candidatelogin.html', {'form': form})

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
                if user.profile_type == User.PROFILE_TYPE_CANDIDATE:
                    return redirect('candidate_dashboard')
                elif user.profile_type == User.PROFILE_TYPE_RECRUITER:
                    return redirect('recruiter_dashboard')
                

            messages.error(request, 'Invalid username or password')

        return render(request, 'matcher/candidatelogin.html', {'form': form})

class UserRLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'matcher/recruiterlogin.html', {'form': form})

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
                if user.profile_type == User.PROFILE_TYPE_CANDIDATE:
                    return redirect('candidate_dashboard')
                elif user.profile_type == User.PROFILE_TYPE_RECRUITER:
                    return redirect('recruiter_dashboard')
                

            messages.error(request, 'Invalid username or password')

        return render(request, 'matcher/recruiterlogin.html', {'form': form})

class CandidateDashboardView(View):
    def get(self, request):
        user = request.user
        if user.profile_type != User.PROFILE_TYPE_CANDIDATE:
            # Only candidates are allowed to view this page
            return redirect('login')

        # Get the posts that are relevant to the user
        posts = Post.objects.filter(skills__in=user.skills)

        return render(request, 'matcher/candidate_dashboard.html', {'posts': posts})

class RecruiterDashboardView(View):
    def get(self, request):
        user = request.user
        if user.profile_type != User.PROFILE_TYPE_RECRUITER:
            # Only recruiters are allowed to view this page
            return redirect('login')

        # Get the posts that the user has created
        posts = Post.objects.filter(Q(is_active=True) & Q(groups__name='mygroup'))

        return render(request, 'matcher/recruiter_dashboard.html', {'posts': posts})

class CandidateOrRecruiterView(View):
    def get(self, request):
        form = CandidateOrRecruiterForm()
        return render(request, 'matcher/candidate_or_recruiter.html', {'form': form})