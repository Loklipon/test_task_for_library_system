from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import EventsViewset, EventCreateView

router = SimpleRouter()
router.register('', EventsViewset)

urlpatterns = [
    path('create/', EventCreateView.as_view(), name='create_organization'),
    path('', include(router.urls)),
]
