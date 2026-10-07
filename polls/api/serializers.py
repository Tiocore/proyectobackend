from rest_framework import serializers
from polls.models import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ['id', 'votes']


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(
        source='choice_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Poll
        fields = ['id', 'event', 'question', 'choices']
        read_only_fields = ['id', 'choices']