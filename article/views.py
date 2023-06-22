from django.shortcuts import render
from django.http import HttpResponse


# ARTICLES

def index_articles(request):
	return HttpResponse('<h1>Блог</h1>')