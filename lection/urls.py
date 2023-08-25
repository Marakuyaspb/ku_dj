from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index_lections, name='lections'),
    path('<int:pk>', views.LectionFullView.as_view(),name='single_page') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

