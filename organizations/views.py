from rest_framework.generics import CreateAPIView

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationCreateView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
