__author__ = 'cemkiy'
from django.conf.urls import patterns, url
from prediction import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^try_ready/$', 'prediction.views.try_ready'),
                    )
