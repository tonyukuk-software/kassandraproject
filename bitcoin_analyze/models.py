from django.db import models

__author__ = 'cemkiy'
# Create your models here.

class rank(models.Model):
    twitter = models.FloatField(default=0.0)
    expected_value = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    change_rate = models.FloatField(default=0.0)


class twitter(models.Model):
    processed_tweets_number = models.SmallIntegerField(default=100)
    positive_tweet_number = models.SmallIntegerField()
    negative_tweet_number = models.SmallIntegerField()
    result = models.BooleanField(default=True)  # main result


class expected_value(models.Model):
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    avg = models.FloatField(default=0.0)
    result = models.BooleanField(default=True)  # main result


class volume(models.Model):
    volume_value = models.FloatField(default=0.0)
    result = models.BooleanField(default=True)  # main result


class change(models.Model):
    change_value = models.FloatField(default=0.0)  # 3.15
    result = models.BooleanField(default=True)  # main result


class change_rate(models.Model):
    change_rate_value = models.FloatField(default=0.0)  # % 0.41
    result = models.BooleanField(default=True)  # main result