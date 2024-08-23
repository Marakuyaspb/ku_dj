import os
from django.db import models
from django.conf import settings


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


class Lection(models.Model):
	lection_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='lection_categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	title = models.CharField(verbose_name ='Название лекции', max_length=200)
	annotation = models.TextField(verbose_name ='Анонс лекции')
	img = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	tags = models.ManyToManyField(Tag, related_name='lectures', blank=True)

	class Meta:
		ordering = ['title']
		indexes = [
			models.Index(fields=['title']),
		]
		verbose_name = 'Лекция'
		verbose_name_plural = 'Лекции'


	def __str__(self):
		return f'Лекция "{self.title}"'
