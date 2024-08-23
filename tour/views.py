import os
from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Tour



def tours(request):
	tours = Tour.objects.all
	context = {
		'tours':tours,
	}
	return render(request, 'tour/tours.html', context)



def the_tour(request, category=None, id=None):
	if id:
		the_tour = get_object_or_404(Tour, tour_id=id)
		similar_tour = Tour.objects.filter(category=the_tour.category)

		context = {
			'the_tour':the_tour,
			'similar_tour':similar_tour,
		}
		return render(request, 'tour/the_tour.html', context)