from django.shortcuts import render
from .models import Notification

def notifications_view(request):
    notifications = Notification.objects.filter(recipient=request.user)
    context = {'notifications': notifications}
    return render(request, 'notifications/notifications.html', context)
