from rest_framework import generics

from .serializers import DeckSerializer
from quizcard.models import Deck


class DeckAPIView(generics.ListCreateAPIView):
    """
    Api for get Deck list and create Deck.
    """
    serializer_class = DeckSerializer

    def get_queryset(self):
        return Deck.objects.filter(owner=self.request.user)

    def perform_create(self, obj):
        obj.save(owner=self.request.user)
