from django.db import models
import os
from django.db import models
from django.conf import settings


class Tag(models.Model):
	id = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=50, verbose_name='Ключевое слово', null=True, blank=True)

	class Meta:
		ordering = ['tag']
		indexes = [
			models.Index(fields=['tag']),
		]
		verbose_name = 'Ключевое слово'
		verbose_name_plural = 'Ключевые слова'

	def __str__(self):
		return self.tag


class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=60, verbose_name='Категория')
	class Meta:
		ordering = ['category']
		indexes = [
			models.Index(fields=['category']),
		]
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'	

	def __str__(self):
		return self.category

class Tour(models.Model):
	tour_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='tour_categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	title_tour = models.CharField(verbose_name ='Название лекции', max_length=200)
	price_single = models.CharField(verbose_name ='Цена для одного', max_length=200, null=True, blank=True)
	price_group = models.CharField(verbose_name ='Цена для группы', max_length=200, null=True, blank=True)
	meet_point = models.CharField(verbose_name ='Точка сборки', max_length=200, null=True, blank=True)
	duration = models.CharField(verbose_name ='Длительность', max_length=200, null=True, blank=True)
	annotation_tour = models.TextField(verbose_name ='Анонс лекции')
	questions = models.TextField(verbose_name ='Вы узнаете ответы')

	img_tour_main = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_1 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_2 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_3 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_4 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_5 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_6 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_7 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_tour_8 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	tags = models.ManyToManyField(Tag, related_name='tours', blank=True)

	class Meta:
		ordering = ['title_tour']
		indexes = [
			models.Index(fields=['title_tour']),
		]
		verbose_name = 'Экскурсия'
		verbose_name_plural = 'Экскурсии'

	def __str__(self):
		return f'Экскурсия "{self.title_tour}"'