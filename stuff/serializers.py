from rest_framework import serializers
from stuff.models import Stuff


class StuffSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    s_name = serializers.HyperlinkedIdentityField(view_name='stuff-name', format='html')

    class Meta:
        model = Stuff
        fields = ['s_name', 'id', 'url', 'owner', 'name', 'descriptions']
