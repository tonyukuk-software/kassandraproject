__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django.db import models
from django.contrib.auth.models import User

# Keeps user's premium expiry date 
class Member_Premium(models.Model):
    user = models.OneToOneField(User)
    premium_expiry_date = models.DateTimeField(auto_now_add=True)

# Keeps package information
class Member_Package(models.Model):
    PACKAGE_CHOICES = (
    (u'0', u'Basic'),
    (u'1', u'Standard'),
    (u'2', u'Premium'),
    )

    package = models.CharField(max_length=1, choices=PACKAGE_CHOICES, default='0')
    pay_amount = models.FloatField(default=0)

# Keeps user's pay information
class Member_Pay(models.Model):
    user = models.ForeignKey(User)
    package = models.ForeignKey(Member_Package)
    pay_amount = models.FloatField(default=0)
    pay_date = models.DateTimeField(auto_now_add=True)

# Keeps user's bitcoin processes
class Bitcoin_Process(models.Model):
    user = models.ForeignKey(User)
    bitcoin = models.FloatField(default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_amount = models.FloatField(default=0)
    sales_date = models.DateTimeField(null=True)
    sales_amount = models.FloatField(null=True)