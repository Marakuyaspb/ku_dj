from django.shortcuts import render
from django.http import HttpResponse

# MAIN PAGE

def index(request):
	return HttpResponse('<h1>Главная</h1>')