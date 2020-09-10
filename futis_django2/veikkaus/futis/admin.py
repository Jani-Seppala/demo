from django.contrib import admin
from .models import Profile, Tulokset, Veikkaukset


class VeikkauksetA(admin.ModelAdmin):
    list_display = ('osallistuja', 'tulokset', 'veikkaus')


admin.site.register(Profile)
admin.site.register(Tulokset)
admin.site.register(Veikkaukset, VeikkauksetA)
# Register your models here.
