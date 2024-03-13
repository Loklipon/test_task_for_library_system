from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['title', 'description', 'address', 'postcode']


class OrganizationWithUserSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True, read_only=True)
    address = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['title', 'description', 'address', 'users']

    def get_address(self, obj):
        return f'{obj.postcode}, {obj.address}'