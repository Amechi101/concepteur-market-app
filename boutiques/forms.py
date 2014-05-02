from __future__ import unicode_literals

from django import forms

from django.forms import extras, ModelForm

from products.models import Boutique

class BoutiqueForm(ModelForm):
	class Meta:
		model = Boutique