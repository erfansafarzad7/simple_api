from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from stuff.models import Stuff
from stuff.serializers import StuffSerializer


class StuffList(APIView):
    def get(self, request, format=None):
        stuff = Stuff.objects.all()
        serializer = StuffSerializer(stuff, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StuffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StuffDetail(APIView):
    def get_object(self, pk):
        try:
            stuff = Stuff.objects.get(pk=pk)
        except Stuff.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        serializer = StuffSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = StuffSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            self.get_object(pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
