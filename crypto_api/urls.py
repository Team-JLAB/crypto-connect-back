from django.urls import path
from .views import WalletGetUpdate, UserView, TransactionViewSet,  WatchlistViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'transactions', TransactionViewSet)
router.register(r'wallet', WalletGetUpdate)
router.register(r'watchlist', WatchlistViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]