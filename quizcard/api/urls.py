from django.urls import path

from .views import DeckAPIView


urlpatterns = [
    path('deck/', DeckAPIView.as_view()),
]
