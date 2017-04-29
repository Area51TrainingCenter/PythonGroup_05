from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from actividades.views import HomeView, ActividadesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^actividades/$', ActividadesView.as_view(), name='actividades'),
    url(r'^$', HomeView.as_view(), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
