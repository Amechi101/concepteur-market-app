from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
# class ProfileUser(models.Models):
# 	user = models.OneToOneField(User)
	
# 	birthday = models.DateField(null=True, blank=True)
# 	city = models.CharField(max_length=50, blank=True)
#     state = models.CharField(max_length=50, blank=True)

#     user_title = models.CharField(max_length=254, verbose_name="Influencer Level", blank=True)
#     user_points = models.IntegerField(null=False, verbose_name="Influence Credit", blank=True)
#     picture = moels.ImageField(upload_to='images', blank=True)

#     #admin level and additional infomation
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     #Override the _unicode_() methid to return out something meaningful
#     def _unicode_(self):
#     	return self.user.username