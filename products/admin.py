from __future__ import unicode_literals

from django.contrib import admin
from products.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "description", "color_name", "size_types", "product_price", "old_price", "product_tags", "novelty","product_website", "image", "slug", "uploaded_by", "uploaded_at", "is_active"]
    search_fields = ["name", "product_price"]
    list_per_page = 25

class ProductCategoryAdmin(admin.ModelAdmin): 

    list_display = ["name", "slug", "is_active", "created_at", "updated_at"]
    search_fields = ["name"]
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


