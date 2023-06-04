from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Ad
from .forms import AdForm
from notifications.utils.notifications import create_notification


@login_required
def create_ad(request):
    if request.method != 'POST':
        form = AdForm()
        return render(request, 'create_ad.html', {'form': form})

    form = AdForm(request.POST)
    if not form.is_valid():
        return render(request, 'create_ad.html', {'form': form})

    ad = form.save()
    if ad:
        create_notification(request.user, ad, "Ваше объявление было успешно создано!")

    form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})


def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})
