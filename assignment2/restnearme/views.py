from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import MichelinRestaurants
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm 
from .models import UserProfile
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# map view function
def map_view(request):
        michelin_restaurants = MichelinRestaurants.objects.all()
        print(michelin_restaurants) # Print all Michelin restaurants in the console for debugging purposes
        return render(request, 'index.html', {'michelin_restaurants': michelin_restaurants}) # Pass the Michelin restaurants to the template
    
# login view function
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # Check if form is valid
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #access UserProfile
                user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={'username': username})
                # Redirect to map page
                return redirect('map_view')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')  #Redirect to login page after logging out

# registration view function
def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            username = form.cleaned_data.get('username')

            # Handle location consent and data
            location_consent = request.POST.get('location_consent') == 'on' # True if checked, False otherwise
            latitude = request.POST.get('latitude') # Get latitude from form
            longitude = request.POST.get('longitude') # Get longitude from form

            if location_consent and latitude and longitude:
                # Convert strings to float
                latitude = float(latitude)
                longitude = float(longitude)
                # Create a geospatial Point
                location = Point(longitude, latitude, srid=4326)
                # Update or create the user profile
                UserProfile.objects.update_or_create(
                    user=user,
                    defaults={
                        'username': username,
                        'email': user.email,
                        'location': location,
                        'location_consent': location_consent
                    }
                )
            # Redirect to login page
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('user_login')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def user_list(request):
    # Get all user profiles that have a location and have consented to share it
    users_with_location = UserProfile.objects.exclude(location__isnull=True).filter(location_consent=True)
    return render(request, 'user_list.html', {'users': users_with_location})

# API endpoint for user list
@login_required
def api_user_list(request):
    users = UserProfile.objects.exclude(location__isnull=True).filter(location_consent=True) # Get all user profiles that have a location and have consented to share it
    user_data = [
        {
            'username': user.user.username,
            'location': {
                'latitude': user.location.y,
                'longitude': user.location.x
            }
        } for user in users
    ]
    return JsonResponse(user_data, safe=False)

