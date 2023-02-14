from django.urls import path

from .views import DeckListAPIView, CurrentDeckAPIView


urlpatterns = [
    path('deck/', DeckListAPIView.as_view()),
    path('deck/<int:pk>/', CurrentDeckAPIView.as_view()),
]
