from django.contrib import admin

from chat.models import *


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display: list[str] = ['id', 'thread_name', 'get_username', 'message', 'timestamp']
    list_per_page: int = 20

    def get_username(self, obj):
        return obj.sender.username if obj.sender else ''

@admin.register(Profile)
class MessageAdmin(admin.ModelAdmin):
    list_display: list[str] = ['get_username', 'phone']
    list_per_page: int = 20

    def get_username(self, obj):
        return obj.user if obj.user else ''

@admin.register(UserProfileModel)
class MessageAdmin(admin.ModelAdmin):
    list_display: list[str] = ['user']
    list_per_page: int = 20

    def get_username(self, obj):
        return obj.user if obj.user else ''