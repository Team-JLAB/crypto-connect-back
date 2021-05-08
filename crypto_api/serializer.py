from rest_framework import serializers
from .models import User, Wallet, Watchlist



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('balance', )
        model = Wallet
    
 



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Wallet.objects.create(user_id=user)
       
        return user

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ('coin', 'user_id' )

 
  