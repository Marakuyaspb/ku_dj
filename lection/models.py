from django.db import models
from django import forms


class Lection(models.Model):
	lection_title = models.CharField('Название лекции', max_length=200)
	lection_annotation = models.TextField('Аннотация лекции')
	lection_header = models.FileField('Картинка для верха страницы')

	def __str__(self):
		return self.lection_title


class Lection_categories(forms.Form):
	CATEGORIES = (
		('1', 'Первая мировая война'),
		('2', 'Вторая мировая война'), 
		('3', 'Революция и Гражданская война'),
		('4', 'Повседневность Санкт-Петербурга Серебряного века'), 
		('5', 'Серебряный век дачной жизни'),
		('6', 'Петроград-Ленград: новый человек в старом городе'),
	)
	lection_category = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CATEGORIES)