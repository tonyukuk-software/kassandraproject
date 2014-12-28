__author__ = 'barisariburnu'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                    url(r'^try_ready/$', 'twitter.views.try_ready'),
                    )
