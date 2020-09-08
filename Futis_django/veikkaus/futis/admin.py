from django.contrib import admin
from .models import Osallistujat, Tulokset, Veikkaukset


class VeikkauksetA(admin.ModelAdmin):
    list_display = ('osallistujat', 'tulokset', 'veikkaus')


admin.site.register(Osallistujat)
admin.site.register(Tulokset)
admin.site.register(Veikkaukset, VeikkauksetA)
# Register your models here.
