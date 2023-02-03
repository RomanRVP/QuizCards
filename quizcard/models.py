from django.db import models
from django.conf import settings


class Deck(models.Model):
    """
    A set of cards assigned to a user.
    """
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class QuizCard(models.Model):
    """
    Quiz card with question and answer.
    """
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
