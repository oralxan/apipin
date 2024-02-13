from django.contrib.admin import *
from .models import CustomUser

@register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username')