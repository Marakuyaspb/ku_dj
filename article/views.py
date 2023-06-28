from django.shortcuts import render

# ARTICLES

def index_articles(request):

	
	return render(request, 'article/single_page.html', {})