# for GET endpoints

from rest_framework import serializers
from .models import SMSData, SMSValDump

class SMSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSData
        fields = '__all__'

class SMSValDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSValDump
        fields = '__all__'

