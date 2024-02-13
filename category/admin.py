from django.contrib.admin import *
from . models import Categorys
@register(Categorys)
class CategorysAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

