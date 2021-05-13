from rest_framework import serializers
from djmoney.money import Money
from .models import User, Wallet, Watchlist, Transaction
from rest_auth.models import TokenModel


class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenModel
        fields = ('key', 'user_id',)


class WalletSerializer(serializers.ModelSerializer):
    def validate_balance(self, balance):
        if balance < 0:
            raise serializers.ValidationError(
                'Wallet balance cannot be less than $0')
        return balance

    class Meta:
        fields = ('user_id', 'balance', )
        model = Wallet
        extra_kwargs = {'user_id': {'read_only': True}}


class UserSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'id', 'wallet')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Wallet.objects.create(user_id=user)
        return user


class WatchlistSerializer(serializers.ModelSerializer):
    def validate_coin(self, coin):
        user_id = self.context['request'].data['user_id']
        coin = coin.lower()
        try:
            obj = self.Meta.model.objects.get(user_id=user_id, coin=coin)
        except self.Meta.model.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError(
                f'user_id {user_id} with coin {coin} already exists')
        return coin

    def validate_user_id(self, user_id):
        if user_id != self.context['request'].user:
            raise serializers.ValidationError(
                'Cannot create transactions for unauthenticated user')
        return user_id

    class Meta:
        model = Watchlist
        fields = ('user_id', 'coin', 'watchlist_id')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('transaction_id', 'user_id', 'units',
                  'price', 'coin', 'transaction_type')
        model = Transaction

    def validate_user_id(self, user_id):
        if user_id != self.context['request'].user:
            raise serializers.ValidationError(
                'Cannot create transactions for unauthenticated user')
        return user_id

    def create(self, validated_data):
        txn = Transaction(**validated_data)
        wallet = Wallet.objects.get(user_id=txn.user_id)

        # IF SALE, VALIDATE ENOUGH UNITS AVALIABLE TO SELL
        if txn.transaction_type == 'SELL':
            coin_queryset = Transaction.objects.filter(
                user_id=txn.user_id, coin=txn.coin)
            coin_txns = [c.units if c.transaction_type ==
                         'BUY' else (c.units * -1) for c in coin_queryset]
            available_units = sum(coin_txns)
            if available_units <= 0:
                raise serializers.ValidationError('Not enough avaliable units')

        # UDPDATE WALLET FUNDS (wallet model will raise error if this goes negative)
        price = txn.price if txn.transaction_type == 'SELL' else txn.price * - 1
        wallet.balance += (price * txn.units)

        # IF PURCHASE, VALIDATE FUNDS
        if txn.transaction_type == "BUY" and wallet.balance < Money(0, 'USD'):
            raise serializers.ValidationError(
                'Wallet balance cannot be less than $0')

        # Save Wallet & Transaction
        wallet.save()
        txn.save()
        return txn
