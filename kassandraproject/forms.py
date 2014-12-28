__author__ = 'barisariburnu'
__author__ = 'cemkiy'

from django import forms

class forgotten_password_form(forms.Form):
    email = forms.CharField(max_length=250)