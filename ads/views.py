from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.conf import settings

from .models import Ad
from .forms import AdForm
from notifications.utils.notifications import create_notification
from .forms import RegistrationForm
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
    ad_list = Ad.objects.all()
    paginator = Paginator(ad_list, settings.ADS_PER_PAGE)

    page_number = request.GET.get('page')
    try:
        page_number = int(page_number)
    except (TypeError, ValueError):
        page_number = 1
    page_obj = paginator.get_page(page_number)

    return render(request, 'ads/ad_list.html', {'page_obj': page_obj})

@login_required
def ad_list_authorized(request):
    ad_list_authorized = Ad.objects.filter(user=request.user)
    paginator = Paginator(ad_list_authorized, settings.ADS_PER_PAGE)

    page_number = request.GET.get('page')
    try:
        page_number = int(page_number)
    except (TypeError, ValueError):
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, 'ads/ad_list.html', {'page_obj': page_obj})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save_user()
            return redirect('login')
    else:
        form = RegistrationForm()
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