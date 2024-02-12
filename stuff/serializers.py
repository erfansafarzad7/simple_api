from rest_framework import serializers
from stuff.models import Stuff


class StuffSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Stuff
        fields = ['owner', 'name', 'descriptions']
