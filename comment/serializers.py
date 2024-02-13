
from rest_framework import serializers
from .models import Commet

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commet
        fields = '__all__'

