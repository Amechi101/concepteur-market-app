from django.db import models

# Create your models here.
class Address(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid_address = models.ForeignKey('Users')
    address = models.CharField(max_length=50L, blank=True)
    city = models.CharField(max_length=50L, blank=True)
    state = models.CharField(max_length=50L, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=30L, blank=True)
    isbilling = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s %s %s %s %s %s' % (self.uid_address, self.address, self.city, self.state, self.zip_code, self.country, self.isbilling)  


class Card(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid_card = models.ForeignKey('Users')
    address_bill = models.ForeignKey('Address')
    cnumber = models.BigIntegerField(null=True, blank=True)
    ccv = models.IntegerField(null=True, blank=True)
    expire = models.DateField(null=True, blank=True)
    name_on_card = models.CharField(max_length=30L, blank=True)
    
    def __unicode__(self):
        return '%s %s %s %s %s %s' % (self.uid_card, self.address_bill, self.cnumber, self.ccv, self.expire, self.name_on_card)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=254L, unique=True)
    password = models.CharField(max_length=255L)
    first_name = models.CharField(max_length=255L, blank=True)
    last_name = models.CharField(max_length=255L, blank=True)
    gender = models.CharField(max_length=1L, blank=True)
    birthday = models.DateField(null=True, blank=True)
    reward_points_current = models.IntegerField(null=True, blank=True)
    reward_points_lifetime = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s %s %s %s' % (self.email, self.password, self.first_name, self.last_name, self.birthday)

