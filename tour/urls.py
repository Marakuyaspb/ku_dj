from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'tour'

urlpatterns = [
    path('tours/', views.tours, name = 'tours'),
    path('tours/<int:id>/', views.the_tour, name='the_tour'),
]