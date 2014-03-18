from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField(null=True,blank=True)
	city = models.CharField(max_length=50,blank=True)
	state = models.CharField(max_length=50,blank=True)
	user_title = models.CharField(max_length=254, verbose_name="Influencer Level", blank=True)
	user_points = models.IntegerField(null=True, verbose_name="Style Points", blank=True)
	image = models.ImageField(upload_to='user_images/',null=True, blank=True)
	

	#admin level and additional infomation
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	#Override the _unicode_() method to return out something meaningful
	def __unicode__(self):
		return ' %s %s %s %s %s %s' % (self.birthday, self.city, self.state, self.image, self.user_title, self.user_points) 

