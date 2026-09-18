from django.db import models
from events.models import Event


class Poll(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text
