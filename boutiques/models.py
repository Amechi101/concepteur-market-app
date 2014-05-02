from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from designers.models import Designer



class Boutique(models.Model):
	name = models.CharField(max_length=254, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)    
	city = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True)
	zipcode = models.IntegerField(max_length=5, null=True, blank=True)
	boutique_website = models.URLField(max_length=200,  null=True, blank=True)

	#For Admin Purposes, to track a product to see which is active by administrative users
	is_active = models.BooleanField(default=True)

	#Foreign Keys & other relationships
	designer = models.ForeignKey(Designer)

	#Metadata
	class Meta:
		verbose_name = _("Boutique Information")
		verbose_name_plural = _("Boutiques")

	#Helps return something meaningful, to show within the admin interface for easy interaction
	def __unicode__(self):
		return "{0}, {1}, {2}".format(self.name, self.city, self.state)
