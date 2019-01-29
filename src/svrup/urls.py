from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from .views import Home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Home.as_view(), name='home'),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^category/', include('category.urls', namespace='category')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^videos/', include('videos.urls', namespace='videos')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
