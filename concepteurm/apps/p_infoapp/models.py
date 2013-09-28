from django.db import models

# Create your models here.
class Address(models.Model):
    id = models.ForeignKey('Users', primary_key=True, db_column='id')
    address = models.CharField(max_length=50L, blank=True)
    city = models.CharField(max_length=50L, blank=True)
    state = models.CharField(max_length=50L, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=30L, blank=True)
    isbilling = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'address'


class Card(models.Model):
    id = models.ForeignKey('Users', primary_key=True, db_column='id')
    cnumber = models.BigIntegerField(null=True, blank=True)
    ccv = models.IntegerField(null=True, blank=True)
    expire = models.DateField(null=True, blank=True)
    name_on_card = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'card'

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
    class Meta:
        db_table = 'users'
