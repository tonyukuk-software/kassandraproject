__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django.db import models

# Keeps robot's bitcoin processes
class Bitcoin_Process_For_Robot(models.Model):
    bitcoin = models.FloatField(default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_amount = models.FloatField(default=0)
    sales_date = models.DateTimeField(null=True)
    sales_amount = models.FloatField(null=True)

    # TODO : Indices will be created by purchase_date : __author__ = 'barisariburnu'