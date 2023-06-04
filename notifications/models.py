from django.db import models
from django.contrib.auth.models import User
from ads.models import Ad

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
