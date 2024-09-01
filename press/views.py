import os
from django.shortcuts import render, get_object_or_404
from .models import Publication


def publications(request):
	publications = Publication.objects.all
	context = {
		'publications':publications,
	}
	return render(request, 'press/press.html', context)