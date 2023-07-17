from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from .models import Notification


def notification_list(request):
    notification_list = Notification.objects.filter(recipient=request.user)
    paginator = Paginator(notification_list, settings.NOTIFICATIONS_PER_PAGE)
    page_number = request.GET.get('page')
    try:
        page_number = int(page_number)
    except (TypeError, ValueError):
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, 'notifications/notifications.html', {'page_obj': page_obj})
