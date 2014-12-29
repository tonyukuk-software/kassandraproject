from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from member.models import Member_Pay

__author__ = 'cemkiy'

from django.shortcuts import render, render_to_response
from bitcoin_analyze.analyze import analyze
from models import *
from datetime import datetime
# Create your views here.
from django.template import RequestContext, Context

@login_required
def guess_bitcoin(request):
    try:
        member_pay = Member_Pay.objects.filter(user=request.user).last()
        if member_pay:
            day_result = datetime.now() - member_pay.pay_date.replace(tzinfo=None)
            print day_result.days
            if member_pay.package == '1':
                if day_result.days > 30:
                    return HttpResponseRedirect('/pricing_table')
            else:
                if day_result.days > 365:
                    return HttpResponseRedirect('/pricing_table')
        else:
            return HttpResponseRedirect('/pricing_table')
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')
    btc_analyze = analyze()
    result_for_bitcoin = btc_analyze.guess_what()
    return render_to_response('guess_bitcoin.html', locals(), context_instance=RequestContext(request))


@login_required
def robot_investor_log(request):
    btc_analyze = analyze()
    print btc_analyze._btcturk.transactions()
    order_list = btc_analyze._btcturk.transactions()
    print order_list
    return render_to_response('robot_investor_log.html', locals(), context_instance=RequestContext(request))
