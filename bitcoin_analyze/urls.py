__author__ = 'cemkiy'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('bitcoin_analyze.views',
                        url(r'^guess_bitcoin/$', 'guess_bitcoin'),
                        url(r'^robot_investor_log/$', 'robot_investor_log'),
                        )