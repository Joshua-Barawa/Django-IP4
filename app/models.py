from django.db import models
from django.contrib.auth.models import User
import datetime


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='media/default2.png', upload_to='media/', null=True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE)
    business_email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)