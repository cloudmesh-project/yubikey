from django.contrib import admin

from models import UserYubi


class YubicoKeyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_id')
    search_fields = ['user', 'device_id']


admin.site.register(UserYubi, YubicoKeyUserAdmin)
