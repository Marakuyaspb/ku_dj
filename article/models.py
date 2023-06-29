from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length=250)
	article_category = models.CharField(max_length=100, default='Пешком по городу')
	article_annotation = models.TextField('Аннотация статьи')
	article_body = RichTextField(default='А я иду, шагаю...')


	def __str__(self):
		return self.article_title
		return self.article_category
