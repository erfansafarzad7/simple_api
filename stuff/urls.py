from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stuff.views import StuffViewSet
from rest_framework import renderers

stuff_list = StuffViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

stuff_details = StuffViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

stuff_name = StuffViewSet.as_view({
    'get': 'name',
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = format_suffix_patterns([
    path('list/', stuff_list, name='stuffs-list'),
    path('<int:pk>/', stuff_details, name='stuff-detail'),
    path('<int:pk>/name', stuff_name, name='stuff-name'),
])

