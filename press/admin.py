from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
	list_display = ['press_title', 'time', 'press_annotation', 'link']
	list_filter = ['press_title']