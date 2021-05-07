from django.urls import path
from .views import WalletGetUpdate, UserViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('wallet/<int:pk>', WalletGetUpdate.as_view(), name='wallet'),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]