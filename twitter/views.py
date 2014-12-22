from django.shortcuts import render, render_to_response
from django.template import RequestContext
from twython import Twython
from django.conf import settings

# Create your views here.
def search_gen_with_OAuth2_Access_Token():
    twitter = Twython(settings.APP_KEY, access_token =settings.OAUTH2_ACCESS_TOKEN)
    data = twitter.search_gen('#bitcoin')
    return data

#example for search_gen_with_OAuth2_Access_Token()
#def try_ready(request):
#    data = search_gen_with_OAuth2_Access_Token()
#    for result in data:
#        result['text'] = Twython.html_for_tweet(result)
#        print(result['text'])

def search_with_OAuth2_Access_Token():
    twitter = Twython(settings.APP_KEY, access_token =settings.OAUTH2_ACCESS_TOKEN)
    data = twitter.search(q='#bitcoin', result_type='recent', count=10)
    return data

#incorrect method
def search_with_OAuth_Token():
    twitter = Twython(settings.APP_KEY, settings.APP_SECRET,
                      settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
    data = twitter.search(q='#bitcoin')
    if data.get('statuses'):
        return data

def try_ready(request):
    data = search_with_OAuth2_Access_Token()
    for result in data['statuses']:
        result['text'] = Twython.html_for_tweet(result)
        print(result['text'])