from rest_framework import generics
from .serializer import WalletSerializer
from .models import Wallet



class WalletGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


