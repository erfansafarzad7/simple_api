from django.urls import path, include
from accounts.views import UserViewSet


from rest_framework.urlpatterns import format_suffix_patterns
user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('list/', user_list, name='user-list'),
    path('<int:pk>/', user_detail, name='user-detail'),
])


