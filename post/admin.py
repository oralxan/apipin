from django.contrib.admin import *
from .models import Post
@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

