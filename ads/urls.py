from django.urls import path
from .views import home
from .views import create_ad
from .views import ad_list
from .views import ad_list_authorized
from .views import register
from .views import user_login
from .views import user_logout

urlpatterns = [
    path('', home, name='home'),
    path('ads/', ad_list, name='ad_list'),
    path('my-ads/', ad_list_authorized, name='ad_list_authorized'),
    path('create-ad/', create_ad, name='create_ad'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
