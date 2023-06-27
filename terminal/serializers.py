from rest_framework import serializers
from .models import *


class PersonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCategory
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
