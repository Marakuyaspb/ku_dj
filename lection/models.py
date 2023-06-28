from django.db import models


class Lection(models.Model):
	lection_title = models.CharField('Название лекции', max_length=200)
	lection_annotation = models.TextField('Аннотация лекции')
	lection_header = models.FilePathField('Картинка для верха страницы', max_length=250)

	def __str__(self):
		return f'Лекция "{self.lection_title}"'