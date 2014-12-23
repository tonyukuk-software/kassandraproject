from django.shortcuts import render, render_to_response
from django.template import RequestContext
from twython import Twython
from django.conf import settings

# Create your views here.
def search_gen_with_OAuth2_Access_Token(word):
    twitter = Twython(settings.APP_KEY, access_token =settings.OAUTH2_ACCESS_TOKEN)
    data = twitter.search_gen(word)
    return data

#example for search_gen_with_OAuth2_Access_Token(word)
#def try_ready(request):
#    data = search_gen_with_OAuth2_Access_Token(word)
#    for result in data:
#        result['text'] = Twython.html_for_tweet(result)
#        print(result['text'])

def search_with_OAuth2_Access_Token(word, max):
    twitter = Twython(settings.APP_KEY, access_token =settings.OAUTH2_ACCESS_TOKEN)
    data = twitter.search(q=word, result_type='recent', count=max)
    return data

#incorrect method
def search_with_OAuth_Token():
    twitter = Twython(settings.APP_KEY, settings.APP_SECRET,
                      settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
    data = twitter.search(q='#bitcoin')
    if data.get('statuses'):
        return data

#Returns a tweet list with the values taken by the parameters
def get_tweets_by_param(word, max):
    data = search_with_OAuth2_Access_Token(word, max)
    tweet_list = []
    for result in data['statuses']:
        result['text'] = Twython.html_for_tweet(result, use_display_url=True, use_expanded_url=True)
        tweet_list.append(result['text'])
    return tweet_list

def try_ready(request):
    tweet_list = []
    i = 1
    tweet_list = get_tweets_by_param('#bitcoin', 15)
    for result in tweet_list:
        print(str(i) + ': ' + result)
        i+=1