from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    CustomUserLoginForm,
    CustomUserUpdateForm,
)


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  # Hash password
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("user:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]  # username field is email in form
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect(
                    "store:laptop_list"
                )  # Change 'home' to your desired redirect URL
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserLoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("user:login")


@login_required
def profile_update_view(request):
    user = request.user
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("user:profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, "accounts/profile_update.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html", {"user": request.user})



