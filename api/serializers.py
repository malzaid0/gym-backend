from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Gym, Class, Booking


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', "email"]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "id"]


class CreateGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ["name", "address", ]


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ["name", "address", "id"]


class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["title", "type", "date", "time", "is_free", "capacity", "gym"]


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["title", "type", "date", "time", "is_free", "capacity", "gym", "available", "id"]


class BookClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["gym_class"]


class BookingSerializer(serializers.ModelSerializer):
    gym_class = ClassSerializer()

    class Meta:
        model = Booking
        fields = ["gym_class", "user"]
