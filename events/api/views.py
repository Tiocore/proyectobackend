from rest_framework import viewsets

from events.models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API RESTful para administrar eventos.
    """

    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer