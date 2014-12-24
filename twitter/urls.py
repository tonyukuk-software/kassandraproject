__author__ = 'barisariburnu'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                    url(r'^login/$', 'twitter.views.login'),
                    url(r'^try_ready/$', 'twitter.views.try_ready'),
                    )
