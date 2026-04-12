app_name = 'accounts'

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
     path('logout/', views.logout_user, name='logout_user'),
]