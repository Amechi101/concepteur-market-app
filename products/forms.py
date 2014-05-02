from __future__ import unicode_literals

from django import forms

from django.forms import extras, ModelForm

from products.models import Product, ProductCategory

     
class ProductForm(ModelForm):
	class Meta:
		model = Product

class ProductCategoryForm(ModelForm):
	class Meta:
		model = ProductCategory