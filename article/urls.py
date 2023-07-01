from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_articles, name='articles'),
    path('quick_add', views.quick_add_art, name='quick_add'),
    path('<int:pk>', views.ArticleFullView.as_view(),name='single_article'),
]
