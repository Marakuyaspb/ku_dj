from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'article_title', 'article_category', 'article_annotation']
	list_editable = ['article_title', 'article_category', 'article_annotation']