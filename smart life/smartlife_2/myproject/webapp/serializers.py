from rest_framework import serializers
from .models import device

class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'