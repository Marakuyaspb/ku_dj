import os
from django.shortcuts import render, get_object_or_404
from .models import Category, Lection, Tag


def lections(request):
	lections = Lection.objects.all
	context = {
		'lections':lections,
	}
	return render(request, 'lection/lections.html', context)


def the_lection(request, category=None, id=None):
	if id:
		the_lection = get_object_or_404(Lection, id=id)
		similar_lections = Lection.objects.filter(category=the_lection.category)

	context = {
		'the_lection':the_lection,
		'similar_lections':similar_lections,
	}
	return render(request, 'lection/the_lection.html', context)