from django.db import models

class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length=200)
	article_annotation = models.TextField('Текст статьи')
	article_header = models.FilePathField('Картинка для верха страницы', max_length=250)

	def __str__(self):
		return self.article_title