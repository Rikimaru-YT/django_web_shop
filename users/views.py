from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import UserLoginForm, UserRegistrationForm



def show_auth_page(request):
    login_form = UserLoginForm()
    registration_form = UserRegistrationForm()
    context = {
        'login_form': login_form,
        'registration_form': registration_form
    }
    return render(request, 'users/auth.html', context)


def login_user(request):
    login_form = UserLoginForm(data=request.POST)
    if login_form.is_valid():
        user = login_form.get_user()
        if user is not None:
            login(request, user)
            return redirect('home')
    return redirect('auth-page')


def register_user(request):
    registration_form = UserRegistrationForm(data=request.POST, files=request.FILES)
    if registration_form.is_valid():
        registration_form.save()
        return redirect('auth-page')
    return redirect('auth-page')


def user_logout(request):
    logout(request)
    return redirect('home')