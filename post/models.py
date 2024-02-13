from django.db.models import *
from user.models import CustomUser
from category.models import Categorys
class Post(Model):
    title = CharField(
        'title of the post',
        max_length=126
    )
    descriptions = TextField(
        'descriptions of the post',
        max_length=526,
        blank=True,
        null= True
    )
    created = DateField(
        'creted date',
        auto_now_add=True
    )
    image = ImageField(
        'imge post',
        upload_to='post_img/'
    )
    user = ForeignKey(
        CustomUser,
        on_delete=PROTECT
    )
    watch_count = IntegerField(
        'prosmotr',
        default=0

    )
    like_count = IntegerField(
        'likes',
        default=0
    )
    category = ForeignKey(
        Categorys, 
        related_name='posts', 
        on_delete=CASCADE)
    def __str__(self) -> str:
        return f'{self.title}'
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



