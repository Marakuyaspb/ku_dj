from django.shortcuts import render

# LECTION SINGLE PAGE

def index_lections(request):
	return render(request, 'main/index_lections.html') 