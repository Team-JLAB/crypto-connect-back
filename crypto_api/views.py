from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializer import WalletSerializer, UserSerializer
from .models import Wallet



class WalletGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny, )