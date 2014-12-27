from kassandraproject import settings

__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kassandraproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^twitter/', include('twitter.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^bitcoin_analyze/', include('bitcoin_analyze.urls')),
    url(r'^$', 'kassandraproject.views.home_page', name='home'),
) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
