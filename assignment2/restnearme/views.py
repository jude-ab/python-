from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import MichelinRestaurants
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm 
from .models import UserProfile

def map_view(request):
        michelin_restaurants = MichelinRestaurants.objects.all()
        print(michelin_restaurants)
        return render(request, 'index.html', {'michelin_restaurants': michelin_restaurants})
    

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #access UserProfile
                user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={'username': username})
                # Redirect map page
                return redirect('map_view')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')  #Redirect to login page after logging out


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})