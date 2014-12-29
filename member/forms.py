__author__ = 'cemkiy'
__author__ = 'barisariburnu'

from django import forms
from django.contrib.auth.models import User

class new_member_form(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput(),
                   'email': forms.EmailInput(),
                   'last_login': forms.HiddenInput(),
                   'is_superuser': forms.HiddenInput(),
                   'is_staff': forms.HiddenInput(),
                   'is_active': forms.HiddenInput(),
                   'date_joined': forms.HiddenInput(),
                   'groups': forms.HiddenInput(),
                   'user_permissions': forms.HiddenInput(),
                   }

class edit_profile_photo_form(forms.Form):
    profile_photo = forms.ImageField()