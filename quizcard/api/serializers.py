from rest_framework import serializers

from quizcard.models import Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'description', 'pk')
