import re

from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers

from empapp.models import User


# class UserSerializer(Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     userpassword = serializers.CharField()
#     age = serializers.IntegerField()
#     salay = serializers.DecimalField(max_digits=10, decimal_places=2)
#     date = serializers.DateTimeField()
#
#
# class UserDeSerializer(Serializer):
#     # id = serializers.IntegerField()
#     username = serializers.CharField()
#     userpassword = serializers.CharField()
#     age = serializers.IntegerField()
#     salay = serializers.DecimalField(max_digits=10, decimal_places=2)
#     date = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

# class UserMODELSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "userpassword", "age", "salay", "date")


class UserDeMoDELSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username", "userpassword", "age", "salay", "date")
        extra_kwargs = {
            "id": {
                "read_only": True
            },
        }

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username")
        instance.save()
        return instance