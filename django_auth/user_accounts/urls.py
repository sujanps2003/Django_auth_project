from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from .views import UserLoginView,signup_view,UserPasswordResetView,change_password,logout_view,dashboard,profile_view


urlpatterns = [
     path('', lambda request: redirect('login'), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('forgot-password/', UserPasswordResetView.as_view(), name='forgot_password'),
    path('forgot-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='user_accounts/password_reset.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user_accounts/confirm_password.html'),name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user_accounts/password_complete.html'),name='password_reset_complete'),
    path('change-password/', change_password, name='change_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]