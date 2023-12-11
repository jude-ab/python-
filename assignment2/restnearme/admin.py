from django.contrib.gis import admin
from .models import MichelinRestaurants, UserProfile

# Register your models here.  
admin.site.register(MichelinRestaurants, admin.GISModelAdmin)
admin.site.register(UserProfile, admin.GISModelAdmin)
