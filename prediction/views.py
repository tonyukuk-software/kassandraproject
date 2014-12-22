from django.shortcuts import render, render_to_response
import google_prediction
# Create your views here.
from google_prediction.models import HostedModel


# def try_ready(request):
#     m = HostedModel('sample.sentiment')
#     print 'cem is not handsome:'
#     print m.predict('cem is not handsome')['outputLabel']
#     return render_to_response('try_ready.html')