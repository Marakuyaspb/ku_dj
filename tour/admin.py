from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Tour, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id', 'category']
	list_filter = ['category']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'tag']
	list_filter = ['tag']

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
	list_display = ['tour_id', 'category', 'title_tour', 'price_single', 'price_group', 'meet_point', 'annotation_tour', 'questions']
	list_filter = ['title_tour']