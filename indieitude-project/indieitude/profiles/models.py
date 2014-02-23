from django.contrib.auth.models import AbstractUser
from django.db import models

#Model for Users
class ProfileUser(AbstractUser):
	birthday = models.DateField(null=True, blank=True)
	city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    hello world
    user_title = models.CharField(max_length=254, verbose_name="" blank=True)
    user_points = models.IntegerField(null=False, blank=True)
    avatar = FileField()

    #admin level and additional infomation
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



