# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('products:home') 
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    context = {
        'page_title': 'Register',
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('products:home') 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    context = {
        'page_title': 'Login',
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('products:home')
