from rest_framework import serializers
from .models import device

class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        #fields = ('device_ID', 'token_Number', 'time')
        fields = '__all__'