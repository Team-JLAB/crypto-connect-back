from django.urls import path
from .views import WalletGetUpdate

urlpatterns = [
    path('wallet/<int:pk>', WalletGetUpdate.as_view(), name='wallet')
]