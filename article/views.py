from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView

# ARTICLES

def index_articles(request):
	articles = Article.objects.all()	
	return render(request, 'main/index_articles.html', {'articles': articles})

def quick_add_art(request):
	form = ArticleForm()
	data = {
		'form':form
	}
	return render(request, 'article/quick_add_art.html', data)

class ArticleFullView(DetailView):
	model = Article
	template_name = 'article/single_page.html'
	context_object_name = 'article'