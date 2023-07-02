from django import forms
from .models import Article
from django.forms import ModelForm, TextInput, ModelChoiceField, ChoiceField


class ArticleForm(ModelForm, ModelChoiceField):
    class Meta:
        model = Article
        fields = ['article_title', 'article_category', 'article_annotation', 'article_body']
        widgets = {
            'article_title': TextInput(attrs={
                'class':'form-control mb-2',
                'placeholder':'Заголовок статьи'
                }),
            'article_category': TextInput(attrs={
                'class':'form-select mb-2',
                'placeholder':'Выбрать категорию'
                }),
            'article_annotation': TextInput(attrs={
                'class':'form-control mb-2',
                'placeholder':'Увлекательное начало статьи'
                }),
            }