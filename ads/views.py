from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .models import Ad
from .forms import AdForm
from notifications.utils.notifications import create_notification
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')

@login_required
def create_ad(request):
    if request.method != 'POST':
        form = AdForm()
        return render(request, 'ads/create_ad.html', {'form': form})

    form = AdForm(request.POST)
    if not form.is_valid():
        return render(request, 'ads/create_ad.html', {'form': form})

    ad = form.save()
    ad.user = request.user
    ad.save()
    if ad:
        create_notification(request.user, ad, "Ваше объявление было успешно создано!")

    form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})


def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})

@login_required
def ad_list_authorized(request):
    ads = Ad.objects.filter(user=request.user)
    return render(request, 'ads/ad_list.html', {'ads': ads})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')