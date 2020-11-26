from rest_framework import serializers
from models import User

class UserSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=32)
    address = serializers.CharField(max_length=45)
    phone_number = serializers.IntegerField(max_length=9)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.login = validated_data.get('login', instance.login)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance