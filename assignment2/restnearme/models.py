from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Created model for Michelin restaurants
class MichelinRestaurants(models.Model):
    city = models.CharField(max_length=100, null=True, default='Unknown')
    latitude = models.FloatField()  
    longitude = models.FloatField()  
    location = models.PointField(srid=4326)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, default='Unknown')
    cuisine = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.region

# user model with one-to-one relationship
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50, null=True)
    location = models.PointField(srid=4326, null=True, blank=True)  #  geolocation
    location_consent = models.BooleanField(default=False) #  geolocation consent