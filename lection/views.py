from django.shortcuts import render
from django.http import HttpResponse

# LECTIONS
def index_lections(request):
	return HttpResponse('main/index.html')
