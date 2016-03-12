from django.contrib import admin
from shinyapps.models import ShinyGroup, ShinyItem

class ShinyItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'dirname', 'itemid')
    list_filter = ('group',)
    ordering = ['group', 'name']

class ShinyGroupAdmin(admin.ModelAdmin):
    list_display = ('username', 'selected')

admin.site.register(ShinyItem, ShinyItemAdmin)
admin.site.register(ShinyGroup, ShinyGroupAdmin)