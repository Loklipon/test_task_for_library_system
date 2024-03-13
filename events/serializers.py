from rest_framework import serializers

from organizations.serializers import OrganizationSerializer, OrganizationWithUserSerializer
from users.serializers import UserSerializer
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    organizations = OrganizationWithUserSerializer(many=True)

    class Meta:
        model = Event
        fields = ['title', 'description', 'organizations', 'image', 'date']
