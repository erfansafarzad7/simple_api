from stuff.models import Stuff
from stuff.serializers import StuffSerializer
from stuff.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, generics, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class StuffViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer, ], url_path='name')
    def stuff_name(self, request, *args, **kwargs):
        stuff = self.get_object()
        return Response(stuff.name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
