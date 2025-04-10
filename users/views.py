from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm
from .models import UserRole


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('users:redirect_by_role')
            else:
                messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def redirect_by_role(request):
    role = request.user.profile.role
    if role == UserRole.OWNER:
        return redirect('properties:owner_dashboard')
    elif role == UserRole.INVESTOR:
        return redirect('properties:investor_dashboard')
    elif role == UserRole.STAFF:
        return redirect('properties:staff_dashboard')
    else:
        return redirect('users:login')