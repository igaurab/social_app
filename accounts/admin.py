

from django.contrib import admin

# Register your models here.
from django.apps import apps

app_config = apps.get_app_config('accounts')
models = app_config.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
