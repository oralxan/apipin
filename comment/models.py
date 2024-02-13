from django.db.models import *
from user.models import CustomUser
from post.models import Post
class Commet(Model):
    user =ForeignKey(
        CustomUser,
        on_delete=PROTECT
    )
    posts = ForeignKey(
        Post,
        on_delete=PROTECT

    )
    comment = TextField(
        'comment',
        max_length=550
    )


