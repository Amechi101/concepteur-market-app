from __future__ import unicode_literals

from django import forms

from django.forms import extras, ModelForm

from designers.models import Designer


class DesignerForm(ModelForm):
	class Meta:
		model = Designer