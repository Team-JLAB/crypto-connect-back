from django.db import models
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField


TRANSACTION_TYPES = (
    ("BUY", "BUY"),
    ("SELL", "SELL")
)


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD', default=10000)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    units = models.PositiveIntegerField(default=1)
    price = MoneyField(max_digits=14, decimal_places=2,
                       default_currency='USD')
    coin = models.CharField(max_length=4)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES, default="BUY")
