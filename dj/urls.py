from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Центр управления начинкой сайта'
admin.site.index_title = 'Админская панель'
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('lection/', include('lection.urls')),
    path('article/', include('article.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
