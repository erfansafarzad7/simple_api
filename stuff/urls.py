from django.urls import path
from stuff import views

urlpatterns = [
    path('list/', views.stuff_list),
    path('<int:pk>/', views.stuff_detail),
]

