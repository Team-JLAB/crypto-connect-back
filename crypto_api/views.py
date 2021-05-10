from rest_framework import viewsets
from .serializer import WalletSerializer, UserSerializer, TransactionSerializer, WatchlistSerializer
from .models import Wallet, User, Transaction, Watchlist
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny



class WalletGetUpdate(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    http_method_names = ['get', 'put', 'head']

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(user_id=user)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['get', 'post', 'head']

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user_id=user)


class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    http_method_names = ['get', 'post', 'head', 'delete']