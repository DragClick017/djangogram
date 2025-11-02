from django.contrib import admin
from apps.bot.models import Users
from unfold.admin import ModelAdmin


@admin.register(Users)
class BotUserAdmin(ModelAdmin):
    list_display = ('chat_id', 'username', 'first_name')
    search_fields = ('chat_id', 'username', 'first_name')
    list_filter = ('first_name',)
