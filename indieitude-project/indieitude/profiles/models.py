# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# #custom user model fro Users
# class MyUser(AbstractBaseUser):
# 	username = models.CharField(max_length=40, db_index=True)
# 	first_name = models.CharField(max_length=254, blank=True)
#     last_name = models.CharField(max_length=254, blank=True)
# 	email = models.EmailField(max_length=254, null=False, unique=True, blank=True)
# 	birthday = models.DateField(null=True, blank=True)
# 	city = models.CharField(max_length=50, blank=True)
#     state = models.CharField(max_length=50, blank=True)
#     user_title = models.CharField(max_length=254, blank=True)
#     user_points = models.IntegerField(null=False, blank=True)
#     avatar = FileField()

#     #admin level and additional infomation
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)



#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email', 'username']


# class MyUserManager(object):
# 	"""Creates and saves a User with the given first_name, last_name, birthday,"""
# 	def create_user(self, email, username, first_name, last_name, birthday, city, state, user_title, user_points, avatar, password=None):
# 		if not email:
# 			raise ValueError('Users must have an email address')

# 		user = self.model(
# 			email=MyUserManager.normalize_email(email),
# 			first_name=first_name,
# 			last_name=last_name,
# 			birthday=birthday,
# 			city=city
# 			state=state,
# 			user_title=user_title,
# 			user_points=user_points,
# 			avatar=avatar,
# 		)

# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user

# 	def create_superuser(self,  email, first_name, last_name, birthday, city, state, user_title, user_points, avatar, password):
# 		user = self.create_user(email,
# 			password=password,
# 			first_name=first_name,
# 			last_name=last_name,
# 			birthday=birthday,
# 			city=city
# 			state=state,
# 			user_title=user_title,
# 			user_points=user_points,
# 			avatar=avatar,
# 		)


<<<<<<< HEAD
# 		user = 
=======
	


def hello(hi):
    print 4 + 5





>>>>>>> 978563c9c036b1e1f6f7cdf8f2479ea3ead41f3e
		



