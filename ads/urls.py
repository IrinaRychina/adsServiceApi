from django.urls import path
from .views import create_ad
from .views import ad_list

urlpatterns = [
    path('ads/', ad_list, name='ad_list'),
    path('create-ad/', create_ad, name='create_ad')
]
