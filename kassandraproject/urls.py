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
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'^accounts/password/$', 'django.contrib.auth.views.password_change'),
    url(r'^accounts/change-password-done/$', 'django.contrib.auth.views.password_change_done'),
    url(r'', include('registration.backends.default.urls')),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^pricing_table/$', 'kassandraproject.views.pricing_table'),
    url(r'^terms/$', 'kassandraproject.views.terms'),
    url(r'^contact_us/$', 'kassandraproject.views.contact_us'),
    url(r'^sorry/$', 'kassandraproject.views.sorry'),
) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
