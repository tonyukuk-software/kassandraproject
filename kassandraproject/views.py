__author__ = 'cemkiy'
__author__ = 'barisariburnu'

# Imports

from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.

def sorry(request):
    return render_to_response('sorry.html', locals(), context_instance=RequestContext(request))

def home_page(request):
    return render_to_response('home_page.html', locals(), context_instance=RequestContext(request))

def pricing_table(request):
    return render_to_response('pricing_table.html', locals(), context_instance=RequestContext(request))

def terms(request):
    return render_to_response('terms.html', locals(), context_instance=RequestContext(request))