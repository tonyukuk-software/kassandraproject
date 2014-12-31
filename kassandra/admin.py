from django.contrib import admin

# Register your models here.

from django.db.models import get_models, get_app

for model in get_models(get_app('member')):
    admin.site.register(model)

for model in get_models(get_app('bitcoin_analyze')):
    admin.site.register(model)