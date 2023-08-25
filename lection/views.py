from django.shortcuts import render
from .models import Lection
from django.views.generic import DetailView


# LECTION SINGLE PAGE

def index_lections(request):
	lections = Lection.objects.all()
	return render(request, 'main/index_lections.html', {'lections': lections})

class LectionFullView(DetailView):
	model = Lection
	template_name = 'lection/single_page.html'
	context_object_name = 'lection'