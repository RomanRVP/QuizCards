from rest_framework import serializers

from quizcard.models import Deck


class DeckSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    owner = serializers.PrimaryKeyRelatedField()

    def create(self, validated_data):
        return Deck.objects.create(**validated_data)
