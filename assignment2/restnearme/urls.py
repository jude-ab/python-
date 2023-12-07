from django.urls import path
from .views import map_view, user_login, user_logout, user_registration

urlpatterns = [
    path('map/', map_view, name='map_view'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_registration, name='user_registration'),
]

