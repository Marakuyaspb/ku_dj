from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Lection, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id', 'category']
	list_filter = ['category']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'tag']
	list_filter = ['tag']

@admin.register(Lection)
class LectionAdmin(admin.ModelAdmin):
	list_display = ['lection_id', 'category', 'title', 'annotation']
	list_filter = ['title']