from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Wallet, Transaction

admin.site.register(Wallet)
admin.site.register(Transaction)


class WalletInline(admin.StackedInline):
    model = Wallet
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (WalletInline, )
