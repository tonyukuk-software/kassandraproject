__author__ = 'barisariburnu'

from django.conf.urls import patterns, url
from prediction import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^login/$', 'twitter.views.login'),
                    url(r'^try_ready/$', 'twitter.views.try_ready'),
                    )
