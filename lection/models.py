from django.db import models
#from django.conf import settings


class Lection(models.Model):
	lection_title = models.CharField('Название лекции', max_length=200)
	lection_annotation = models.TextField('Аннотация лекции')
	#lection_header = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)

	def __str__(self):
		return f'Лекция "{self.lection_title}"'