from rest_framework import serializers
from django.utils.timezone import now
from .models import Event, Category, Registration, Location
from django.contrib.auth.models import User


# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source="organizer.username")

    class Meta:
        model = Event
        fields = '__all__'

    def validate_date_time(self, value):
        if value < now():
            raise serializers.ValidationError("Event date must be in the future.")
        return value

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

    def validate(self, data):
        event = data.get("event")
        if event.registrations.count() >= event.capacity:
            raise serializers.ValidationError("Event is fully booked.")
        return data
