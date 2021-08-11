from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    username = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20)
    id = serializers.IntegerField(read_only=True)

