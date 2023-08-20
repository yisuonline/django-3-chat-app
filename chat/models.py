from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.sender.username}-{self.thread_name}' if self.sender else f'{self.message}-{self.thread_name}'

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)
    phone = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
class UserProfileModel(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=100)
    online_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username