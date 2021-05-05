from rest_framework import generics, viewsets
from .serializer import WalletSerializer, UserSerializer
from .models import Wallet, User


class WalletGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer