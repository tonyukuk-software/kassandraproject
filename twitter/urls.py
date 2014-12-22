__author__ = 'barisariburnu'

from django.conf.urls import patterns, url
from prediction import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^twitter/$', 'twitter.views.login'),

                       )
