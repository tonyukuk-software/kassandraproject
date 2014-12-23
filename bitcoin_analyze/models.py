from django.db import models
from kassandraproject import settings
__author__ = 'cemkiy'
# Create your models here.

class Rank(models.Model):
    twitter = models.FloatField(default=20.0)
    expected_value = models.FloatField(default=20.0)
    volume = models.FloatField(default=20.0)
    change = models.FloatField(default=20.0)
    change_rate = models.FloatField(default=20.0)
    main_result = models.BooleanField(default=True)


class Twitter(models.Model):
    processed_tweets_number = models.SmallIntegerField(default=100)
    positive_tweet_number = models.SmallIntegerField()
    negative_tweet_number = models.SmallIntegerField()
    result = models.BooleanField(default=True)  # main result


class Expected_Value(models.Model):
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    last = models.FloatField(default=0.0)
    result = models.BooleanField(default=True)  # main result


class Volume(models.Model):
    volume_value = models.FloatField(default=0.0)
    result = models.BooleanField(default=True)  # main result


class Change(models.Model):
    change_value = models.FloatField(default=0.0)  # 3.15
    result = models.BooleanField(default=True)  # main result


class Change_Rate(models.Model):
    change_rate_value = models.FloatField(default=0.0)  # % 0.41
    result = models.BooleanField(default=True)  # main result