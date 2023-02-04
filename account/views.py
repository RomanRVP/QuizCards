from django import views
from django.shortcuts import render


class RegistrationAndLogin(views.View):
    """
    A class that is responsible for creating a new account and logging into it.
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'account/signup_and_signin.html')
