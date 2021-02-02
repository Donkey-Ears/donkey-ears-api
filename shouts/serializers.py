from rest_framework import serializers as sz
from .models import Shout
from users.serializers import UserSerializer


class ShoutSerializer(sz.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Shout
        fields = ("id", "user", "text")
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        shout = Shout.objects.create(user=request.user, **validated_data)
        return shout

    def update(self, instance, validated_data):
        request = self.context.get("request")
        instance.text = validated_data.get("text", instance.text)
        instance.save()
        return instance
