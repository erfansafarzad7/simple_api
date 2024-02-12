from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stuff import views

urlpatterns = [
    path('list/', views.stuff_list),
    path('<int:pk>/', views.stuff_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
