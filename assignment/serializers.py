import email
from unittest.util import _MAX_LENGTH

from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.EmailField(max_length=50, min_length=6)
    last_name = serializers.CharField(max_length=50, min_length=6)
    email = serializers.CharField(max_length=150, write_only=True)
    password1 = serializers.CharField(max_length=50,min_length=8)
    password2 = serializers.CharField(max_length=50,min_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('first_name', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(first_name=first_name).exists():
            raise serializers.ValidationError({'first_name': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)