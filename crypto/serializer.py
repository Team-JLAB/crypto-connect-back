from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('create_date', 'update_date', 'balance')
        model = Wallet
