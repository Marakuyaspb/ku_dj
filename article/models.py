from django.db import models
from django_quill.fields import QuillField
#from ckeditor.fields import RichTextField


class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length=250)
	article_annotation = models.TextField('Аннотация статьи')
	article_body = QuillField('Текст', default='А я иду, шагаю...')

	def __str__(self):
		return self.article_title
		return self.article_annotation
		return self.article_body

	GO = 'GO'
	SZ = 'SZ'
	BY = 'BY'
	W1 = 'W1'
	W2 = 'W2'
	HP = 'HP'
	HA = 'HA'
	HB = 'HB'
	AR = 'AR'
	SE = 'SE'

	CATEGORIES_CHOISES = [
		('GO', 'Пешком по городу'),
		('SZ', 'Вокруг Петербурга'),
		('BY', 'Старый быт'),
		('W2', 'Вторая мировая'),
		('W1', 'Первая мировая'),
		('HP', 'Истории людей'),
		('HA', 'Истории зверей'),
		('HB', 'Книжные истории'),
		('AR', 'Искусство'),
		('SE', 'Секреты')
	]
	article_category = models.CharField(max_length=2, choices=CATEGORIES_CHOISES)