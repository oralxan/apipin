from rest_framework import serializers
from .models import Categorys

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = '__all__'

