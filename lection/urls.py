from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'lection'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lections/', views.lections, name = 'lections'),
    path('tours/', views.tours, name = 'tours'),
    path('contact/', views.contact, name = 'contact'),

    path('lections/<int:id>/', views.the_lection, name='the_lection'),
    path('tours/<int:id>/', views.the_tour, name='the_tour'),
]