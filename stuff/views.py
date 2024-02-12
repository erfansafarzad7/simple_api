from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from stuff.models import Stuff
from stuff.serializers import StuffSerializer


@csrf_exempt
def stuff_list(request):
    if request.method == 'GET':
        stuff = Stuff.objects.all()
        serializer = StuffSerializer(stuff, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StuffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def stuff_detail(request, pk):
    try:
        stuff = Stuff.objects.get(pk=pk)
    except Stuff.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = StuffSerializer(stuff)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StuffSerializer(stuff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stuff.delete()
        return JsonResponse(status=204)
