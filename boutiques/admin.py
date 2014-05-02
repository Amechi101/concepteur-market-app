from __future__ import unicode_literals

from django.contrib import admin
from boutiques.models import Boutique


class BoutiqueAdmin(admin.ModelAdmin):

	list_display = ["name", "address", "city", "state", "zipcode", "boutique_website", "is_active"]
	search_fields = ["name"]
	list_per_page = 10


#Register Models below
admin.site.register(Boutique, BoutiqueAdmin)

