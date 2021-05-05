from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 
from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('create_date', 'update_date', 'balance')
        model = Wallet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Wallet.objects.create(user_id=user)
        return user