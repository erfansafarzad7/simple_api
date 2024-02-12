from rest_framework import generics
from stuff.models import Stuff
from stuff.serializers import StuffSerializer


class StuffList(generics.ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
