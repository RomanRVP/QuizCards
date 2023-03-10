from rest_framework import generics

from .serializers import DeckSerializer, QuizCardSerializer
from quizcard.models import Deck, QuizCard
from .permissions import AccessForTheOwnerOfTheDeck

class DeckListAPIView(generics.ListCreateAPIView):
    """
    Api for get Deck list and create Deck.
    """
    serializer_class = DeckSerializer

    def get_queryset(self):
        return Deck.objects.filter(owner=self.request.user)

    def perform_create(self, obj):
        obj.save(owner=self.request.user)


class CurrentDeckAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Api for working with current Deck.
    """
    serializer_class = DeckSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Deck.objects.filter(owner=self.request.user)


class CreateQuizCardAPIView(generics.CreateAPIView):
    """
    Api to create a new quiz-card.
    """
    serializer_class = QuizCardSerializer
    permission_classes = (AccessForTheOwnerOfTheDeck,)

