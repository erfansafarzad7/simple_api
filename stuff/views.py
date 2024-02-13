from stuff.models import Stuff
from stuff.serializers import StuffSerializer
from stuff.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, generics, renderers
from rest_framework.response import Response


class StuffName(generics.GenericAPIView):
    queryset = Stuff.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer, ]

    def get(self, request, *args, **kwargs):
        stuff = self.get_object()
        return Response(stuff.name)


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
