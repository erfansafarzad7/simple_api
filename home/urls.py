from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import UserViewSet
from stuff.views import StuffViewSet

router = DefaultRouter()
router.register(r'stuffs', StuffViewSet, basename='stuff')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
