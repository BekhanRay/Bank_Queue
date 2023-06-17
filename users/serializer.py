from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    # def create(self, validated_data):
    #     user = Users.objects.create(**validated_data)
    #     return user
