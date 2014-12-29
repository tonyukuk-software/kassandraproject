__author__ = 'barisariburnu'
__author__ = 'cemkiy'

from django import forms

class forgotten_password_form(forms.Form):
    email = forms.CharField(max_length=250)


class contact_us_form(forms.Form):
    subjact = forms.CharField(max_length=250)
    name = subjact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    message = forms.CharField(max_length=500)