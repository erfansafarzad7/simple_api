from rest_framework import generics
from stuff.models import Stuff
from stuff.serializers import StuffSerializer
from stuff.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class StuffList(generics.ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StuffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
