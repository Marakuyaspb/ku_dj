from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_articles, name='home_article')
]
