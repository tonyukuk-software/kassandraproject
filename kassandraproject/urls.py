from django.conf.urls import patterns, include, url

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
)
