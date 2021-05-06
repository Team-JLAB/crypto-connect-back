from rest_framework import serializers
from .models import User, Wallet
from djmoney.money import Money

class WalletSerializer(serializers.ModelSerializer):
    def validate_balance(self, balance):
        if balance < 0:
            raise serializers.ValidationError('Wallet balance cannot be less than $0')
        return balance
    
    class Meta:
        fields = ('balance', )
        model = Wallet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Wallet.objects.create(user_id=user)
        return user