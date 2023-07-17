from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404 and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return response
