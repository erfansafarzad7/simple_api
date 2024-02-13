from django.urls import include, path
from rest_framework import routers
from home import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
])
