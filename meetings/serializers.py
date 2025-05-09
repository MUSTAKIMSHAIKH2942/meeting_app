from rest_framework import serializers
from .models import Meeting, Participant

class ParticipantSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Participant
        fields = ['id', 'user', 'user_username', 'joined_at']

class MeetingSerializer(serializers.ModelSerializer):
    host_username = serializers.CharField(source='host.username', read_only=True)
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = [
            'id', 'host', 'host_username', 'title', 'description',
            'start_time', 'end_time', 'room_id', 'created_at', 'participants'
        ]
