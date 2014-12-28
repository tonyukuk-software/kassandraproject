__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django.db import models
from django.contrib.auth.models import User

# Keeps user's premium expiry date
class Member(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/")


# Keeps user's pay information
class Member_Pay(models.Model):
    user = models.ForeignKey(User)
    package = models.CharField(max_length=3, default='1')
    pay_amount = models.FloatField(default=0)
    pay_date = models.DateTimeField(auto_now_add=True)