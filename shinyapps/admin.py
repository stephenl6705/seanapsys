from django.contrib import admin
from .models import ShinyGroup, ShinyItem

admin.site.register(ShinyItem)
admin.site.register(ShinyGroup)