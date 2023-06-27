from django.shortcuts import render
from django.http import HttpResponse

# MAIN PAGE


def index(request):
	return render(request, 'main/index.html')

def contact(request):
	return render(request, 'main/contact.html')

