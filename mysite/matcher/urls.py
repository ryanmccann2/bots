# matcher/urls.py
from django.urls import path
from .views import UserSignupView, UserLoginView, CandidateDashboardView, RecruiterDashboardView
from . import views as matcher_views

urlpatterns = [
    path('', matcher_views.home, name="home"),
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("rdashboard", RecruiterDashboardView.as_view(), name="recruiter_dashboard"),
    path("cdashboard", CandidateDashboardView.as_view(), name="candidate_dashboard"),
]