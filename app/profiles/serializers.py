from .models import CustomUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import validators
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validators.UniqueValidator(
        CustomUser.objects.all())])

    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password
                                                 ])

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "username")
