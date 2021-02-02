from rest_framework import serializers as sz
from .models import User


class UserSerializer(sz.ModelSerializer):
    password = sz.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", "gender", "age")
        read_only_fields = ("id",)

    def validate_username(self, value):
        if ("@", "+") in value:
            raise sz.ValidationError('Username에 "@" 또는 "+"를 사용할 수 없습니다.')
        return value

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
