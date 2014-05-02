from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Designer(models.Model):
	name = models.CharField(max_length=254, blank=True, null=True)
	label_name = models.CharField(max_length=254, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	specialites = models.CharField(max_length=254,  null=True, blank=True)
	image = models.ImageField(upload_to='images/designers/main',max_length=100, null=True) #For the argument upload_to, will add to the static folder and generated image will be stored in suing that path specified

	#For Admin Purposes, to track and see which if still active by for administrative users only
	is_active = models.BooleanField(default=True)


	#Metadata
	class Meta:
		verbose_name = _("Designer Information")
		verbose_name_plural = _("Designers")

	#Helps return something meaningful, to show within the admin interface for easy interaction
	def __unicode__(self):
		return "{0} {1}".format(self.name, self.label_name)
