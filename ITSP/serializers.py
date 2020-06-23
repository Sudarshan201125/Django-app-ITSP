from rest_framework import serializers

from .models import Teams

class TeamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teams
        fields = ('Team_name', 'Team_id', 'Team_members')