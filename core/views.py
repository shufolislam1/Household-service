from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import User, ServicePurchase
from services.models import Services

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
    client = request.user
    purchase = ServicePurchase.objects.filter(client=client)
    if request.user.is_admin:
        # user = request.user
        users = User.objects.filter(is_admin=False)
        user_data = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }
        return render(request, 'profile.html', {'users': users, 'user_data': user_data})
    user_data = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }
    return render(request, 'profile.html', {'user_data': user_data, 'purchase': purchase})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        
        profile_form = forms.ChangeUserForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            user = profile_form.save(commit=False)
            # If a new profile picture is uploaded, save it
            profile_picture = request.FILES.get('profile_picture')
            print(profile_picture)
            if profile_picture:
                user.profile_picture = profile_picture
            user.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})

@login_required
def promote_to_admin(request):
    if request.method == 'POST':
        user_ids = request.POST.getlist('user_ids')
        users_to_promote = User.objects.filter(id__in=user_ids)
        for user in users_to_promote:
            user.is_admin = True
            user.save()
        # Add success message if needed
        messages.success(request, 'Promoted to admin Successfully')
    return redirect('profile')

def take_service(request, service_id):
    if request.user.is_authenticated:
        service = Services.objects.get(id=service_id)
        client = request.user
        ServicePurchase.objects.create(service=service, client=client)
        messages.success(request, 'Service purchased successfully!')
        # return redirect('profile')
        purchases = ServicePurchase.objects.filter(client=request.user)  # Filter by logged-in user
        print(purchases)
        return render(request, 'profile.html', {'purchases': purchases})
    else:
        messages.warning(request, 'You need to be logged in to purchase a service.')
        return redirect('userLogin')