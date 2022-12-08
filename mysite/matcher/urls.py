# matcher/urls.py
from django.urls import path
from .views import UserSignupView, UserLoginView
from . import views as matcher_views

urlpatterns = [
    path('', matcher_views.home, name="home"),
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
]