from django.shortcuts import render
from .models import Lection

# LECTION SINGLE PAGE

def index_lections(request):
	lections = Lection.objects.all()
	return render(request, 'main/index_lections.html', {'lections': lection}) 