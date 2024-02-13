from django.urls import path
from .views import postsss,detail
urlpatterns = [
    path('post/',postsss),
    path('post/<int:pk>/',detail)   
]

