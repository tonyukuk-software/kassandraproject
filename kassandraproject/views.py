__author__ = 'cemkiy'
# Imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def sorry(request):
    return render_to_response('sorry.html', locals(), context_instance=RequestContext(request))