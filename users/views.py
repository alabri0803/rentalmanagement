from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import UserRole


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:redirect_by_role')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    return render(request, 'users/login.html')

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
        messages.error(request, 'لم يتم تحديد دور المستخدم بشكل صحيح.')
        return redirect('users:login')