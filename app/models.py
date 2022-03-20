from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='media/default2.png', upload_to='media/', null=True, blank=True)
    caption = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Neighbourhood(models.Model):
    name = models.CharField()
    location = models.CharField()
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey()
