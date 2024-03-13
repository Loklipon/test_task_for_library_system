from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Organization, Event
from .serializers import EventSerializer


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['date']
