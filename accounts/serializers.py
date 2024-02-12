from django.contrib.auth.models import User
from rest_framework import serializers
from stuff.models import Stuff


class UserSerializer(serializers.ModelSerializer):
    user_stuffs = serializers.PrimaryKeyRelatedField(many=True, queryset=Stuff.objects.all())

    class Meta:
        model = User
        fields = ['user_stuffs', 'id', 'username']
