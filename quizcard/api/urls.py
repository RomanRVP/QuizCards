from django.urls import path

from .views import DeckListAPIView


urlpatterns = [
    path('deck/', DeckListAPIView.as_view()),
]
