# matcher/urls.py
from django.urls import path
from .views import UserSignupView, UserRLoginView, UserCLoginView, CandidateOrRecruiterView
from . import views as matcher_views

urlpatterns = [
    path('', matcher_views.home, name="home"),
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("recruiterlogin/", UserRLoginView.as_view(), name="recruiterlogin"),
    path("candidatelogin/", UserCLoginView.as_view(), name="candidatelogin"),
    # path("rdashboard/", RecruiterDashboardView.as_view(), name="recruiter_dashboard"),
    # path("cdashboard/", CandidateDashboardView.as_view(), name="candidate_dashboard"),
    path("corr/", CandidateOrRecruiterView.as_view(), name="candidate_or_recruiter"),
]