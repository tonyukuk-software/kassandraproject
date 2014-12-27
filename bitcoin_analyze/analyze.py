import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kassandraproject.settings")
from twitter.views import twython_api
from bitcoin_analyze.models import Rank, Expected_Value, Volume, Change, Change_Rate
from btcturk_client.client import Btcturk
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import google_prediction
from google_prediction.models import HostedModel

__author__ = 'cemkiy'
# -*- coding: utf-8 -*-

class analyze:
    def __init__(self):
        self._btcturk = Btcturk("54991feb7d7e11ae3c336333", "LEbkyPYfySnvP4AhiJa58TdROlw+TsYs")
        self.twitter = True
        self.expected_value = True
        self.volume = True
        self.change = True
        self.change_rate = True
        self.main_result = True

    def guess_what(self):
        self.twitter = self.guess_twitter()
        self.expected_value = self.guess_expected_value()
        self.volume = self.guess_volume()
        self.change = self.guess_change()
        self.change_rate = self.guess_change_rate()

        last_ranks = Rank.objects.last()
        if not last_ranks:
            last_ranks = Rank()
            last_ranks.save()

        high_result = 0.0
        low_result = 0.0

        if self.twitter:
            high_result += last_ranks.twitter
        else:
            low_result += last_ranks.twitter

        if self.expected_value:
            high_result += last_ranks.expected_value
        else:
            low_result += last_ranks.expected_value

        if self.volume:
            high_result += last_ranks.volume
        else:
            low_result += last_ranks.volume

        if self.change:
            high_result += last_ranks.change
        else:
            low_result += last_ranks.change

        if self.change_rate:
            high_result += last_ranks.change_rate
        else:
            low_result += last_ranks.change_rate

        if high_result > low_result:
            self.main_result = True
        else:
            self.main_result = False

        return self.main_result


    def get_now_ask_price(self):
        return float(self._btcturk.ticker()['ask'])


    def send_new_rank(self):
        old_rank = Rank.objects.last()
        set_new_ranks = Rank()
        right_list = []
        wrong_list = []

        if self.twitter == self.main_result:
            right_list.append(self.twitter)
        else:
            wrong_list.append(self.twitter)

        if self.expected_value == self.main_result:
            right_list.append(self.expected_value)
        else:
            wrong_list.append(self.expected_value)

        if self.volume == self.main_result:
            right_list.append(self.volume)
        else:
            wrong_list.append(self.volume)

        if self.change == self.main_result:
            right_list.append(self.change)
        else:
            wrong_list.append(self.change)

        if self.change_rate == self.main_result:
            right_list.append(self.change_rate)
        else:
            wrong_list.append(self.change_rate)


        for element in wrong_list:
            if element == self.twitter:
                if old_rank.twitter <= 0:
                    wrong_list.remove(self.twitter)
                else:
                    set_new_ranks.twitter = old_rank.twitter - 2
            elif element == self.expected_value:
                if old_rank.expected_value <= 0:
                    wrong_list.remove(self.expected_value)
                else:
                    set_new_ranks.expected_value = old_rank.expected_value - 2
            elif element == self.volume:
                if old_rank.volume <= 0:
                    wrong_list.remove(self.volume)
                else:
                    set_new_ranks.volume = old_rank.volume - 2
            elif element == self.change:
                if old_rank.change <= 0:
                    wrong_list.remove(self.change)
                else:
                    set_new_ranks.change = old_rank.change - 2
            else:
                if old_rank.change_rate <= 0:
                    wrong_list.remove(self.change_rate)
                else:
                    set_new_ranks.change_rate = old_rank.change_rate - 2

        distribution_points = (2 * len(wrong_list)) / len(right_list)
        for element in right_list:
            if element == self.twitter:
                set_new_ranks.twitter = old_rank.twitter + distribution_points
            elif element == self.expected_value:
                set_new_ranks.expected_value = old_rank.expected_value + distribution_points
            elif element == self.volume:
                set_new_ranks.volume = old_rank.volume + distribution_points
            elif element == self.change:
                set_new_ranks.change = old_rank.change + distribution_points
            else:
                set_new_ranks.change_rate = old_rank.change_rate + distribution_points



        try:
            set_new_ranks.save()
        except Exception as e:
            print e


    def guess_twitter(self):
        t_api = twython_api()
        tweet_list = t_api.search(word='bitcoin', type='mixed', max=5)
        positive_counter = 0
        negative_counter = 0
        m = HostedModel('sample.sentiment')
        for tweet in tweet_list:
            if m.predict(tweet)['outputLabel'] == 'positive':
                positive_counter += 1
            else:
                negative_counter += 1
        if positive_counter > negative_counter:
            return True
        else:
            return False


    def guess_expected_value(self):
        high = float(self._btcturk.ticker()['high'])
        low = float(self._btcturk.ticker()['low'])
        last = float(self._btcturk.ticker()['ask'])
        result = True

        if (high - last) > (last - low):
            result = False
        else:
            result = True

        try:
            expected_value = Expected_Value(high=high, low=low, last=last, result=result)
            expected_value.save()
        except Exception as e:
            print e

        return result


    def guess_volume(self):
        try:
            volume_past = Volume.objects.last()
        except Exception as e:
            print e

        volume_now = float(self._btcturk.ticker()['volume'])
        result = True

        if not volume_past:
            return True

        if volume_now >= volume_past.volume_value:
            result = True
        else:
            result = False

        try:
            new_volume = Volume(volume_value=volume_now, result=result)
            new_volume.save()
        except Exception as e:
            print e

        return result

    def guess_change(self):
        change_value = float(self._btcturk.ticker()['ask']) - float(self._btcturk.ticker()['open'])
        result = True
        page = urllib2.urlopen("https://www.btcturk.com/")
        soup = BeautifulSoup(page)
        span = soup.findAll("span", {"class": "glyphicon glyphicon-chevron-up"})
        if span:
            result = True
        else:
            result = False

        try:
            new_change = Change(change_value=change_value, result=result)
            new_change.save()
        except Exception as e:
            print e

        return result


    def guess_change_rate(self):
        change_rate_value = 100 / float(self._btcturk.ticker()['open'])
        result = True

        if change_rate_value >= 1:
            result = True
        else:
            result = False

        try:
            new_change_rate = Change_Rate(change_rate_value=change_rate_value, result=result)
            new_change_rate.save()
        except Exception as e:
            print e

        return result

# a = analyze()
# print a.guess_twitter()
