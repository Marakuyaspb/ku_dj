from django.shortcuts import render

# ARTICLES

def index_articles(request):
	#articles = Article.objects.all()	
	#return render(request, 'main/index_articles.html', {'articless': article})
	return render(request, 'main/index_articles.html', {})
