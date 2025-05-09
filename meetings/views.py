from rest_framework import viewsets, permissions
from .models import Meeting, Participant
from .serializers import MeetingSerializer, ParticipantSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by('-created_at')
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('-joined_at')
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]
