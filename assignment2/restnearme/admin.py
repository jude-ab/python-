from django.contrib.gis import admin
from .models import MichelinRestaurants, UserProfile
# Register models here.

admin.site.register(MichelinRestaurants, admin.OSMGeoAdmin)
admin.site.register(UserProfile, admin.OSMGeoAdmin)