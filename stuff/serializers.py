from rest_framework import serializers
from stuff.models import Stuff


class StuffSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Stuff
        fields = ['id', 'url', 'owner', 'name', 'descriptions']
