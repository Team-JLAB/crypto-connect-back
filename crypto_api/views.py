from rest_framework import generics, viewsets
from .serializer import WalletSerializer, UserSerializer, WatchlistSerializer
from .models import Wallet, User, Watchlist


class WalletGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer





