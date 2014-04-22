from __future__ import unicode_literals

from django.contrib import admin
from products.models import Designer, Product, ProductCategory, Boutique

class DesignerAdmin(admin.ModelAdmin):
    list_display = ["name", "label_name", "description", "specialites", "image", "is_active"]
    search_fields = ["name", "label_name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "color_name", "size_types", "product_price", "old_price", "product_tags", "novelty","product_website", "image", "slug", "uploaded_by", "uploaded_at", "is_active"]
    search_fields = ["name", "product_price"]

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active", "created_at", "updated_at"]
    search_fields = ["name"]

class BoutiqueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "city", " state", "zipcode", "boutique_website", "is_active"]
    search_fields = ["name"]

admin.site.register(Boutique)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(ProductCategory)


