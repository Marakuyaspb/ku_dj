from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'lection'

urlpatterns = [
    path('lections/', views.lections, name = 'lections'),
    path('lections/<int:id>/', views.the_lection, name='the_lection'),
]