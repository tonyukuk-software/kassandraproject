import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kassandraproject.settings")
from bitcoin_analyze.models import Rank, Expected_Value, Volume, Change, Change_Rate
from btcturk_client.client import Btcturk
import urllib2
from BeautifulSoup import BeautifulSoup

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


    def guess_what(self):
        self.twitter = self.guess_twitter()
        self.expected_value = self.guess_expected_value()
        self.volume = self.guess_volume()
        self.change = self.guess_change()
        self.change_rate = self.guess_change_rate()


        try:
            set_new_ranks = Rank(twitter=self.twitter, expected_value=self.expected_value, volume=self.volume,
                                 change=self.change, change_rate=self.change_rate)
            set_new_ranks.save()
        except Exception as e:
            print e



        print self._btcturk.ticker()


    def guess_twitter(self):
        return True


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

a = analyze()
a.guess_what()
