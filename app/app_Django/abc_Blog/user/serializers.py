from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo', 'profession', 'about', 'birthday', 'twitter', 'linkedin', 'facebook']
        extra_kwargs = {
            'photo': {'required': False},
            'profession': {'required': False},
            'about': {'required': False},
            'birthday': {'required': False},
            'twitter': {'required': False},
            'linkedin': {'required': False},
            'facebook': {'required': False},
        }

class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        return instance

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'fullname', 'profile']