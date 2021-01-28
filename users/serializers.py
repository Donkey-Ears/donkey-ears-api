from rest_framework import serializers as sz
from .models import User


class UserSerializer(sz.ModelSerializer):
    password = sz.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "gender", "age")

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
