from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UserProfileForm
from .models import UserRole  # Assuming you have a UserRole model

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally assign a default role to the user
            # user.userrole_set.create(role='default_role_name')
            login(request, user)
            return redirect('home')  # Redirect to the desired page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the desired page after successful login
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

# User profile view
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the desired page after logout

# Optional: User role management views
def manage_user_roles(request):
    # Implement logic to manage user roles (assign, remove, etc.)
    pass

def assign_role(request, user_id, role_id):
    # Implement logic to assign a specific role to a user
    pass

def remove_role(request, user_id, role_id):
    # Implement logic to remove a specific role from a user
    pass