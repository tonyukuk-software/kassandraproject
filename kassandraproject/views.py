from django.contrib.auth.models import User

__author__ = 'cemkiy'
__author__ = 'barisariburnu'

# Imports

from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from hashids import Hashids
from mailgun import *

# Create your views here.

def sorry(request):
    return render_to_response('sorry.html', locals(), context_instance=RequestContext(request))


def home_page(request):
    return render_to_response('home_page.html', locals(), context_instance=RequestContext(request))


def pricing_table(request):
    return render_to_response('pricing_table.html', locals(), context_instance=RequestContext(request))


def terms(request):
    return render_to_response('terms.html', locals(), context_instance=RequestContext(request))

def forgotten_password(request):
    text_for_result = ''
    form = forgotten_password_form()
    if request.method == 'POST':
        form = forgotten_password_form(request.POST)
        if form.is_valid():
            try:
                email = request.POST.get('email')
                member = User.objects.filter(email=email)[0]
                hashids = Hashids()
                hashid = hashids.encrypt(member.username)
                member.set_password(str(hashid))
                if member:
                    context = Context({'username': member.username, 'password': str(hashid)})
                    mailgun_operator = mailgun()
                    mailgun_operator.send_mail_with_html(email_to=member.email, template_name='mail_forgotten_password.html', context=context, subject='Forgotten Password')
                    text_for_result = 'We are send your password to your email.'
                else:
                    text_for_result = 'Wrong mail address.'
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('forgotten_password.html', locals(), context_instance=RequestContext(request))


def contact_us(request):
    form = contact_us_form()
    if request.method == 'POST':
        form = contact_us_form(request.POST)
        if form.is_valid():
            try:
                subject = request.POST.get('subject')
                email = request.POST.get('email')
                name = request.POST.get('name')
                message = request.POST.get('message')

                mailgun_operator = mailgun()
                mailgun_operator.send_mail('se.cemkiy@gmail.com', name + message + email, subject)
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('contact_us.html', locals(), context_instance=RequestContext(request))