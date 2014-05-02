from __future__ import unicode_literals

from django.contrib import admin
from designers.models import Designer


class DesignerAdmin(admin.ModelAdmin):

	list_display = ["name", "label_name", "description", "specialites", "image", "is_active"]
	search_fields = ["name", "label_name"]
	list_per_page = 50


#Register Models below
admin.site.register(Designer, DesignerAdmin)