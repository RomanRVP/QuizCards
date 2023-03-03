from rest_framework import permissions
from quizcard.models import Deck


class AccessForTheOwnerOfTheDeck(permissions.IsAuthenticated):
    """
    To work with decks and cards in them, you must be their author
    (created to prevent other users from interacting with your data).
    """

    def has_permission(self, request, view):
        return Deck.objects.get(
            pk=view.kwargs.get('deck_id')).owner == request.user
