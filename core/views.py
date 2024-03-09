from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'registered successful')
            return redirect('userLogin')

    else:
        register_form = forms.RegistrationForm()
    return render(request, 'login_register.html', {'form':register_form, 'type':'Register'})

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password = user_pass)
            if user is not None and user.is_admin:
                messages.success(request,'login successful as admin')
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_client:
                messages.success(request,'login successful as client')
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'login info incorrect')
                return redirect('register')
            
    else:
        form = AuthenticationForm()
    return render(request,'login_register.html', {'form': form, 'type':'Login'})
    
def userLogout(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('userLogin')


@login_required
def profile(request):
    user_data = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }
    
    return render(request, 'profile.html', {'user_data': user_data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


def home(request):
    return render(request, 'home.html')

