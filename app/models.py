from django.db import models
from django.contrib.auth.models import User
import datetime


class Neighborhood(models.Model):
    name = models.CharField()
    location = models.CharField()
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey()

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='media/default2.png', upload_to='media/', null=True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Business(models.Model):
    name = models.CharField()
    user = models.ForeignKey(User)
    neighborhood = models.ForeignKey(Neighborhood)
    business_email = models.EmailField()

    def __str__(self):
        return str(self.name)