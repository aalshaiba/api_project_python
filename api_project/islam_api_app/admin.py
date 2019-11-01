from django.contrib import admin
from .fatwas import Fatwas


class FatwasAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)


admin.site.register(Fatwas, FatwasAdmin)