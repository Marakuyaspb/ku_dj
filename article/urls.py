from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_articles, name='articles'),
    path('<int:pk>', views.ArticleFullView.as_view(),name='single_article'),
]
