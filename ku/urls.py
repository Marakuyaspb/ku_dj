from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from blog import views, urls
from main import views, urls
from lection import views, urls
from press import views, urls
from tour import views, urls

admin.site.site_header = 'Система Централизованного Управления Контентом'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('main.urls')),
    path('', include('lection.urls')),
    path('', include('press.urls')),
    path('', include('tour.urls')),
]


urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)