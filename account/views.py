from django import views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView

from .models import User


class RegistrationAndLogin(views.View):
    """
    A class that is responsible for creating a new account and logging into it.
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'account/signup_and_signin.html')

    def post(self, request, *args, **kwargs):
        data = request.POST

        # Sign up -> sign in.
        if 'post-registration-btn' in data:
            user_email = data.get('input-email')
            user_password_1 = data.get('input-password-1')
            user_password_2 = data.get('input-password-2')

            if User.objects.filter(email=user_email):
                return render(request, 'account/signup_and_signin.html',
                              {'ERROR': 'This email already taken!'})
            if user_password_1 != user_password_2:
                return render(request, 'account/signup_and_signin.html',
                              {'ERROR': 'Passwords do not match!'})

            User.objects.create_user(user_email, user_password_1)
            user = authenticate(email=user_email, password=user_password_1)
            login(request, user)
            return redirect('main_page')

        # Sign in.
        elif 'post-login-btn' in data:
            user_email = data.get('input-email')
            user_password = data.get('input-password')
            user = authenticate(email=user_email, password=user_password)
            if user:
                login(request, user)
                return redirect('main_page')

            elif User.objects.filter(email=user_email):
                return render(request, 'account/signup_and_signin.html',
                              {'ERROR': 'Password is not correct!'})

            return render(request, 'account/signup_and_signin.html',
                          {'ERROR': 'User not found!'})


class UserLogOut(LogoutView):
    next_page = 'reg_and_log'
