from django.shortcuts import render, render_to_response
from django.template import RequestContext
from twython import Twython
from django.conf import settings

# Create your views here.
class twython_api:
    def __init__(self):
        self.TWITTER = Twython(settings.APP_KEY, access_token=settings.ACCESS_TOKEN)

    def search(self, word, type=None, max=None):
        # Only search
        if type == None and max == None:
            data = self.TWITTER.search(q=word)
            return data

        # Search with Recent Type
        elif max == None:
            # result_type:
            # Specifies what type of search results you would prefer to receive.
            # The current default is 'mixed'.
            # Valid values include:
                # mixed: Include both popular and real time results in the response.
                # popular: Return only the most recent results in the response.
                # popular: Return only the most popular results in the response.
            data = self.TWITTER.search(q=word, result_type=type)
            return data

        # Search with Recent Type and Count
        else:
            # count:
            # The number of tweets to return per page, up to a maximum of 100.
            # Defaults to 15.
            # This was formerly the 'rpp' parameter in the old Search API.
            data = self.TWITTER.search(q=word, result_type=type, count=max)
            return data

    # Returns Generator
    def search_gen(self, word):
        # This function offers a generator for search results
        data = self.TWITTER.search_gen(word)
        return data

        # Use of search_gen
        # twitter = twython_api()
        # data = twitter.search_gen('#bitcoin')
        # for result in data:
        #     print(result)

    # Don't use for search_gen. Only use for search.
    def get_tweet_list_by_html(self, data):
        tweet_list = []
        for result in data['statuses']:
            result['text'] = Twython.html_for_tweet(result, use_display_url=True, use_expanded_url=True)
            tweet_list.append(result['text'])
        return tweet_list

        # Use of search
        # twitter = twython_api()
        # data = twitter.search('#bitcoin', 'recent', 100)
        # tweet_list = twitter.get_tweet_list_by_html(data)
        #     for result in tweet_list:
        #         print(result)

def try_ready(request):
    tweet_list = []
    i = 1
    twitter = twython_api()
    data = twitter.search('#bitcoin')
    tweet_list = twitter.get_tweet_list_by_html(data)
    for result in tweet_list:
        print(str(i) + ': ' + result)
        i+=1