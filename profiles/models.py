from django.db import models

from django.contrib.auth.models import User
=======
import secretballot
# from django.contrib.auth.models import User



class ProfileUser(models.Model):
	user = models.OneToOneField(User,unique=True)
	birthday = models.DateField(null=True,blank=True)
	city = models.CharField(max_length=50,blank=True)
	state =models.CharField(max_length=50,blank=True)

	# user_title = models.CharField(max_length=254, verbose_name="Influencer Level", blank=True)
	# user_points = models.IntegerField(null=False, verbose_name="Influence Credit", blank=True)
	# picture = models.ImageField(upload_to='images', blank=True)


	#admin level and additional infomation
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	#Override the _unicode_() method to return out something meaningful
	def _unicode_(self):
		return self.user.username
=======
#     #Override the _unicode_() methid to return out something meaningful
#     def _unicode_(self):
#     	return self.user.username

class Comment(models.Models):
	time_posted=models.DateField([auto_now=True, auto_now_add=True])
	body=models.TextField();

secretballot.enable_voting_on(Comment)
>>>>>>> FETCH_HEAD
