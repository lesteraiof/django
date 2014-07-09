from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.static import serve
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('demo.apps.home.urls')),
    url(r'^', include('demo.apps.ventas.urls')),
    url(r'^',include('demo.apps.webServices.wsProductos.urls')),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
)
	