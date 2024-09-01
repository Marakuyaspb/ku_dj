import os
from django.db import models
from django.conf import settings


class Publication(models.Model):
	press_id = models.AutoField(primary_key=True)
	press_title = models.CharField(verbose_name ='Название публикации', max_length=200)
	time = models.DateTimeField(null=True, blank=True)
	press_annotation = models.TextField(verbose_name ='Текст', null=True, blank=True)
	screen_1 = models.ImageField(upload_to='press/', verbose_name = 'Скрин 1', null=True, blank=True)
	screen_2 = models.ImageField(upload_to='press/', verbose_name = 'Скрин 2', null=True, blank=True)
	link = models.TextField(verbose_name ='Ссылка на источник')

	class Meta:
		ordering = ['press_title']
		indexes = [
			models.Index(fields=['press_title']),
		]
		verbose_name = 'Публикация'
		verbose_name_plural = 'Публикации'


	def __str__(self):
		return f'Публикация "{self.press_title}"'