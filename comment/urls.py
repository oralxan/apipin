from django.urls import path
from .views import comments,detail
urlpatterns = [
    path('comment/',comments),
    path('comment/<int:pk>/',detail)   
]

