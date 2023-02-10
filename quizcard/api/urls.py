from django.urls import path

from .views import DeckAPIView


urlpatterns = [
    path('', DeckAPIView.as_view()),
]
