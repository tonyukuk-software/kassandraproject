from member.coinbase_api import coinbase_api
from member.models import Member_Pay, Activation

__author__ = 'cemkiy'
__author__ = 'barisariburnu'

# Imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from member.forms import *
import uuid

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
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            member_user_auth = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            member_user_auth.is_staff = False
            member_user_auth.is_active = False
            member_user_auth.save()

            member = User.objects.filter(username=username)[0]
            code = str(uuid.uuid4())
            activation = Activation.objects.create(activivation_code=code, user=member)
            activation.save()

            # TODO send activation code to user __author__ = 'barisariburnu'

            return HttpResponseRedirect('/accounts/login/')
    return render_to_response('new_member.html', locals(), context_instance=RequestContext(request))


@login_required
def member_profile(request):
    try:
        member = User.objects.filter(username=request.user.username)[0]
        return render_to_response('member_profile.html', locals(), context_instance=RequestContext(request))
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


@login_required
def payment_page(request, package_id):
    if package_id == 1:
        pay_amount = 3
        redirect_url = 'montly'
    else:
        pay_amount = 30
        redirect_url = 'yearly'

    api = coinbase_api()
    order_id = str(request.user.id)
    button = api.create_button(amount=pay_amount, order_id=order_id, package_id=package_id)
    button_data = button[0]
    return render_to_response('payment_page.html', locals(), context_instance=RequestContext(request))


@login_required
def success_url(request, order_id, package_id):
    clean_package_id = ''
    for letter in str(package_id):
        if letter == '?':
            clean_package_id = int(clean_package_id)
            break
        else:
            clean_package_id += letter

    api = coinbase_api()
    coinbase_order = api.get_order_by_id(clean_package_id)

    if coinbase_order:
        print coinbase_order[2]
        if str(coinbase_order[2]) == 'Status.complete': #control for payment
            if clean_package_id == 1:
                pay_amount = 3
            else:
                pay_amount = 30

            try:
                user = User.objects.filter(id=order_id)[0]
                member_pay = Member_Pay(user=user, package=clean_package_id, pay_amount=pay_amount)
                member_pay.save()
                return render_to_response('success_url.html', locals(), context_instance=RequestContext(request))
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')


def cancel_url(request):
    return render_to_response('cancel_url.html', locals())


def user_activation(request, identity):
    try:
        active = Activation.objects.filter(activivation_code=identity)[0]
        user = User.objects.filter(id=active.user.id)[0]
    except:
        return HttpResponseRedirect('/sorry')
    try:
        if user:
            user.is_active = True
            user.is_staff = True
            user.save()
            active.delete()
            return HttpResponseRedirect('/accounts/login/')
    except:
        return HttpResponseRedirect('/sorry')