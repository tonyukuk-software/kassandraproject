__author__ = 'cemkiy'
__author__ = 'barisariburnu'

# Imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from member.forms import *


# Create your views here.
def new_member(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/member/member_profile/')

    form = new_member_form
    if request.method == 'POST':
        form = new_member_form(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            member_user_auth = User.objects.create_user(username, email, password)
            member_user_auth.is_staff = False
            member_user_auth.is_active= False
            member_user_auth.save()
            return HttpResponseRedirect('/accounts/login/')
    return render_to_response('new_member.html', locals(), context_instance=RequestContext(request))

@login_required
def member_profile(request):
    try:
        member = User.objects.filter(username=request.user.username)[0]
        return render_to_response('member_profile.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

@login_required
def edit_profile_photo(request):
    try:
        member = User.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    form = edit_profile_photo_form()

    if request.method == 'POST':
        form = edit_profile_photo_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                member.profile_photo = request.FILES["profile_photo"]
                member.save()
                return HttpResponseRedirect('/member/member_profile')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')

    return render_to_response('edit_profile_photo.html', locals(), context_instance=RequestContext(request))

def success_url(request):
    pass

def payment_page(request):
    pass