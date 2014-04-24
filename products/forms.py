from __future__ import unicode_literals

from django import forms

from django.forms import extras, ModelForm

from products.models import Designer, Product, ProductCategory, Boutique

class DesignerForm(ModelForm):
	class Meta:
		model = Designer
      
class ProductForm(ModelForm):
	class Meta:
		model = Product
       
class BoutiqueForm(ModelForm):
	class Meta:
		model = Boutique

class ProductCategoryForm(ModelForm):
	class Meta:
		model = ProductCategory