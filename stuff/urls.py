from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stuff.views import StuffViewSet

router = DefaultRouter()
router.register(r'stuffs', StuffViewSet, basename='stuff')

urlpatterns = [
    path('', include(router.urls)),
]
