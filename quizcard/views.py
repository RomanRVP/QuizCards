from django import views
from django.shortcuts import render


class HomePage(views.View):
    """
    This is the main page.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'quizcard/main_page.html')
