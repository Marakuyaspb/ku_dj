from django.contrib import admin
from .models import Lection


@admin.register(Lection)
class LectionAdmin(admin.ModelAdmin):
	list_display = ['id', 'lection_title', 'lection_annotation', 'lection_pic']
	list_editable = ['lection_title', 'lection_annotation']
	list_per_page = 5
	search_fields = ['lection_title', 'lection_annotation']