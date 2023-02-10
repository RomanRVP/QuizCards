from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DeckSerializer
from quizcard.models import Deck

class DeckAPIView(APIView):
    """
    Api view for working with the Deck model.
    """
    def get(self, request):
        deck_list = Deck.objects.filter(owner=request.user)
        return Response(
            {'deck_list': DeckSerializer(deck_list, many=True).data}
        )

    def post(self, request):
        serializer = DeckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response({'deck': serializer.data})
