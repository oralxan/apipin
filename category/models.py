from django.db.models import *
class Categorys(Model):
    name = CharField(
        'name',
        max_length=128,

    )
    img = ImageField(
        'img',
        upload_to='category_img/'
    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Categorys'
        verbose_name_plural = 'Categorys'