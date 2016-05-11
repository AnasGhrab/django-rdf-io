from django.conf.urls import patterns, include, url
from .views import to_rdf
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rdf_io.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'to_rdf/(?P<model>[^\/]+)/(?P<id>\d+)$', to_rdf, name='to_rdf'),
    url(r'^admin/', include(admin.site.urls)),
)
