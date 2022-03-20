from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='login-user/')
def index(request):
    return render(request, 'html/index.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('index-page')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
                print(error)
                return render(request, 'html/register.html', {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


@login_required(login_url='login-user/')
def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        profile.profile_pic = request.FILES['profile_pic']
        profile.caption = request.POST.get("bio")

        user = User.objects.filter(username=user.username).update(username=username, first_name=fullname, email=email)
        profile.save()
    return render(request, 'html/profile.html', {"profile": profile})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-page')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'html/login.html', {})

    return render(request, 'html/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login-user')
