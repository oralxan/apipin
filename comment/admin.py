from django.contrib.admin import *

from .models import Commet
@register(Commet)
class CommetAdmin(ModelAdmin):
    list_display = ('id','posts')
    list_display_links = ('id','posts')
