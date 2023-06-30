from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView

# ARTICLES

def index_articles(request):
	articles = Article.objects.all()	
	return render(request, 'main/index_articles.html', {'articles': articles})

class ArticleFullView(DetailView):
	model = Article
	template_name = 'article/single_page.html'
	context_object_name = 'article'