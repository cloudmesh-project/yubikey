from django.contrib import admin

from .models import UserYubi


class YubicoKeyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_id')
    list_display = ('device_id', 'device_id')


admin.site.register(UserYubi, YubicoKeyUserAdmin)
