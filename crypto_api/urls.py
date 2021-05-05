from django.urls import path
from .views import WalletGetUpdate, UserCreate

urlpatterns = [
    path('wallet/<int:pk>', WalletGetUpdate.as_view(), name='wallet'),
    path('account/register', UserCreate.as_view(), name='register')
]