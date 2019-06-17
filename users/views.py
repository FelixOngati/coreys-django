from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created! You are now able to login')
            return redirect('login')
        else:
            form = UserRegisterForm(request.POST)
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        u_profile = ProfileUpdateForm(request.POST,
                                      request.FILES,
                                      instance=request.user.profile)
        if u_form .is_valid() and u_form.is_valid():
            u_form.save()
            u_profile.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        u_profile = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'u_profile': u_profile
    }

    return render(request, 'users/profile.html', context)
