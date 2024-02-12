from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from stuff.models import Stuff
from stuff.serializers import StuffSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def stuff_list(request, format=None):
    if request.method == 'GET':
        stuff = Stuff.objects.all()
        serializer = StuffSerializer(stuff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StuffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def stuff_detail(request, pk, format=None):
    try:
        stuff = Stuff.objects.get(pk=pk)
    except Stuff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StuffSerializer(stuff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StuffSerializer(stuff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stuff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
