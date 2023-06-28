from django import forms
from .models import *


class Lection_categories(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['cat'].empty_label = "Выбрать категорию"


	class Meta:
		model = Lection
		fields = ['lection_title','lection_annotation','lection_header']

	# CATEGORIES = (
	# 	('1', 'Первая мировая война'),
	# 	('2', 'Вторая мировая война'), 
	# 	('3', 'Революция и Гражданская война'),
	# 	('4', 'Повседневность Санкт-Петербурга Серебряного века'), 
	# 	('5', 'Серебряный век дачной жизни'),
	# 	('6', 'Петроград-Ленград: новый человек в старом городе'),
	# )
	# lection_category = forms.ChoiceField(
    #     widget=forms.RadioSelect, choices=CATEGORIES)