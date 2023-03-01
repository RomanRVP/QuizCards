from rest_framework import serializers

from quizcard.models import Deck, QuizCard


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'description', 'pk')


class QuizCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCard
        fields = ('question', 'answer', 'deck')
