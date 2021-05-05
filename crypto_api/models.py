from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


TRANSACTION_TYPES = (
    ("BUY", "BUY"),
    ("SELL", "SELL")
)


class Wallet(models.Model):
    user_id = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    balance = MoneyField(max_digits=14, decimal_places=2,
                         default_currency='USD', default=10000)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    units = models.PositiveIntegerField(default=1)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    coin = models.CharField(max_length=4)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES, default="BUY")


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=64)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)
