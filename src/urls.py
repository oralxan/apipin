
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('posts/',include('post.urls')),
    path('categorys/',include('category.urls')),
    path('comment/',include('comment.urls'))
         
   

]
