from django.shortcuts import render, render_to_response
from bitcoin_analyze.analyze import analyze
from models import *
# Create your views here.
from django.template import RequestContext, Context

def guess_bitcoin(request):
    btc_analyze = analyze()
    result_for_bitcoin = btc_analyze.guess_what()
    return render_to_response('guess_bitcoin.html', locals(), context_instance=RequestContext(request))

def robot_investor_log(request):
    btc_analyze = analyze()
    print btc_analyze._btcturk.transactions()
    order_list = btc_analyze._btcturk.transactions()
    print order_list
    return render_to_response('robot_investor_log.html', locals(), context_instance=RequestContext(request))
