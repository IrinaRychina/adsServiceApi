from django.urls import path
from .views import notifications_view

urlpatterns = [
    path('notifications/', notifications_view, name='notifications')
]
