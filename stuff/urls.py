from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stuff import views

urlpatterns = [
    path('list/', views.StuffList.as_view()),
    path('<int:pk>/', views.StuffDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
