from django.contrib import admin
from .submodels import *
from django.apps import apps

for model in apps.get_app_config('products').models.values():
	admin.site.register(model)