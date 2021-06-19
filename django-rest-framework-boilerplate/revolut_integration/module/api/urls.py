from django.urls import path
from .views import (
   RevolutAccounts,
   RevolutSpecificAccount,
   RevolutBalanceOnAccount,
   RevolutCreateOrder,
   RevolutSendTranasction,
)

urlpatterns = [
    path('accounts', RevolutAccounts.as_view(), name='list'),
    path('account/<int:pk>/', RevolutSpecificAccount.as_view(), name='list'),
    path('account/<int:pk>/balance', RevolutBalanceOnAccount.as_view(), name='list'),
    path('createOrder', RevolutCreateOrder.as_view(), name='list'),
    path('transaction/send', RevolutSendTranasction.as_view(), name='create'),
]
