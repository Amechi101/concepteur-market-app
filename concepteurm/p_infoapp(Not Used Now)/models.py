from django.db import models

# Create your models here.
# class Address(models.Model):
#     id = models.ForeignKey('Users', primary_key=True, db_column='id')
#     address = models.CharField(max_length=50L, blank=True)
#     city = models.CharField(max_length=50L, blank=True)
#     state = models.CharField(max_length=50L, blank=True)
#     zip_code = models.IntegerField(null=True, blank=True)
#     country = models.CharField(max_length=30L, blank=True)
#     billing = models.BooleanField()

#     def __unicode__(self):
#         return '%s %s %s %s %s %s' % (self.address, self.city, self.state, self.zip_code, self.country, self.billing)  


# class Users(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=254L, unique=True)
#     password = models.CharField(max_length=255L)
#     first_name = models.CharField(max_length=255L, blank=True)
#     last_name = models.CharField(max_length=255L, blank=True)
#     gender = models.CharField(max_length=1L, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     reward_points_current = models.IntegerField(null=True, blank=True)
#     reward_points_lifetime = models.IntegerField(null=True, blank=True)
    
#     def __unicode__(self):
#         return '%s %s %s %s %s' % (self.email, self.password, self.first_name, self.last_name, self.birthday)

