from rest_framework import serializers
from .models import *

class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deadline
        fields = '__all__'
        many = True 