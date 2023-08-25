import os
from django.db import models
from django.conf import settings


def pic_path():
	return os.path.join(settings.MEDIA_ROOT, "img")

class Lection(models.Model):
	lection_title = models.CharField('Название лекции', max_length=200)
	lection_annotation = models.TextField('Аннотация лекции')
	lection_pic = models.FilePathField(path=pic_path, default='lection_hall.jpg')

	def __str__(self):
		return f'Лекция "{self.lection_title}"'
		return self.lection_annotation