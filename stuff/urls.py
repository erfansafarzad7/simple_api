from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stuff import views

urlpatterns = format_suffix_patterns([
    path('list/', views.StuffList.as_view(), name='stuffs-list'),
    path('<int:pk>/', views.StuffDetail.as_view(), name='stuff-detail'),
    path('<int:pk>/name', views.StuffName.as_view(), name='stuff-name'),
])

