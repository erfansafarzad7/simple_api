from django.contrib.auth.models import User
from rest_framework import serializers
from stuff.models import Stuff


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_stuffs = serializers.HyperlinkedRelatedField(many=True, view_name='stuff-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'user_stuffs', 'id', 'username']
