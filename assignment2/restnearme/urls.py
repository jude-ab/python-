from django.urls import path
from .views import map_view, user_login, user_logout, user_registration, api_user_list

urlpatterns = [
    path('map/', map_view, name='map_view'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_registration, name='user_registration'),
    path('api/users/', api_user_list, name='api_user_list'),
]

