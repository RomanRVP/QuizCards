from django.urls import path

from .views import DeckListAPIView, CurrentDeckAPIView, CreateQuizCardAPIView


urlpatterns = [
    path('deck/', DeckListAPIView.as_view()),
    path('deck/<int:pk>/', CurrentDeckAPIView.as_view()),
    path('deck/create_quizcard/', CreateQuizCardAPIView.as_view()),
]
