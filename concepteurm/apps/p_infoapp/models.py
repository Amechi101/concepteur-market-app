from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=254L, unique=True)
    password = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L, blank=True)
    last_name = models.CharField(max_length=255L, blank=True)
    gender = models.CharField(max_length=1L, blank=True)
    birthday = models.DateField(null=True, blank=True)
    reward_points_current = models.IntegerField(null=True, blank=True)
    reward_points_lifetime = models.IntegerField(null=True, blank=True)


