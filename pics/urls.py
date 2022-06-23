from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pics'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^search/', views.search_results, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
