from django.urls import path, incl
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('contact', views.contact, name='contact')
]
