from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Todo
        fields = '__all__'