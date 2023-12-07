from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import MichelinRestaurants

# Define the field mappings based on the shapefile's attributes
michelin_restaurants = {
    'name': 'name',           # Field 'name' in the shapefile
    'latitude': 'latitude',   # Field 'latitude' in the shapefile
    'longitude': 'longitude', # Field 'longitude' in the shapefile
    'city': 'city',           # Field 'city' in the shapefile
    'location': 'Point',
    'region': 'region',       # Field 'region' in the shapefile
    'cuisine': 'cuisine',     # Field 'cuisine' in the shapefile
    'price': 'price',         # Field 'price' in the shapefile
    'url': 'url',             # Field 'url' in the shapefile
}

# Path to the shapefile
michelin_restaurants_shp = Path(__file__).resolve().parent / 'data' / 'one-star-michelin-restaurants.shp'

def run(verbose=True):
    lm = LayerMapping(MichelinRestaurants, michelin_restaurants_shp, michelin_restaurants, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)
