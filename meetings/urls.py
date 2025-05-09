from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, ParticipantViewSet

router = DefaultRouter()
router.register(r'meetings', MeetingViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
