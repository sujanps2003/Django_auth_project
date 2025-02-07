from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView , PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user_accounts/login.html'


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request , 'user_accounts/signup.html' , {'form':form})

class UserPasswordResetView(PasswordResetView):
    template_name = 'user_accounts/forget_password.html'

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_accounts/change_password.html', {'form': form})


@login_required
def dashboard(request):
    return render(request , 'user_accounts/dashboard.html', {'username' : request.user.username})

@login_required
def profile_view(request):
    return render(request, 'user_accounts/profile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')