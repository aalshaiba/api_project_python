from django.contrib import admin
from .fatwas import Fatwas, Droosuae


class FatwasAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'muftee')


class DroosUAEAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'shaikh')


admin.site.register(Fatwas, FatwasAdmin)
admin.site.register(Droosuae, DroosUAEAdmin)
