from rest_framework import generics
from .models import Categorys
from .serializers import CategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer
