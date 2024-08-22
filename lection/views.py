import os
from django.shortcuts import render
from .models import Category, Lection, Tag, Tour, Type


def error_404_view(request, exception):
	return render(request, 'lection/404.html', status=404)


def index(request):
	return render(request, 'lection/index.html')
def contact(request):
	return render(request, 'lection/contact.html')


def lections(request):
	lections = Lection.objects.filter(type_id=1)
	context = {
		'lections':lections,
	}
	return render(request, 'lection/lections.html', context)

def tours(request):
	tours = Lection.objects.filter(type_id=2)
	context = {
		'tours':tours,
	}
	return render(request, 'lection/tours.html', context)


def the_lection(request, category=None, id=None):
	if id:
		the_lection = get_object_or_404(Lection, id=id)
		similar_lections = Lection.objects.filter(category=the_lection.category)

	context = {
		'the_lection':the_lection,
		'similar_lections':similar_lections,
	}
	return render(request, 'lection/the_lection.html', context)


def the_tour(request, category=None, id=None):
	if id:
		the_tour = get_object_or_404(Tour, id=id)
		similar_tour = Tour.objects.filter(category=the_tour.category)

	context = {
		'the_tour':the_tour,
		'similar_tour':similar_tour,
	}
	return render(request, 'lection/the_tour.html', context)