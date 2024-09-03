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


class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='lection_categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	title = models.CharField(verbose_name ='Название статьи', max_length=200)
	text = models.TextField(verbose_name ='Текст статьи')
	img_article = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')

	img_article_1 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_article_2 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_article_3 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	img_article_4 = models.ImageField(upload_to='lection/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')

	tags = models.ManyToManyField(Tag, related_name='lectures', blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['title']
		indexes = [
			models.Index(fields=['title']),
		]
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


	def __str__(self):
		return f'Статья "{self.title}"'


	def latest_3_articles(request):
		latest_articles = Article.objects.order_by('-updated_at')[:3]
		return render(request, 'latest_articles.html', {'_articles': _articles})


	def first_two_sentences(self):
		sentences = self.text.split('. ')

		if len(sentences) > 1:
		    return '. '.join(sentences[:2]) + '.'
		elif sentences:
		    return sentences[0] + '.'
		return ''