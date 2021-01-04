from django.contrib import admin
from .models import *


class UrlAdmin(admin.ModelAdmin):
    list_display = ("id", "url")


class ParseAdmin(admin.ModelAdmin):
    list_display = ("content", )


admin.site.register(Url, UrlAdmin)
admin.site.register(ParsingInfo, ParseAdmin)



