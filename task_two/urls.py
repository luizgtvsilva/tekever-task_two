from django.urls import path
from task_two.views import *

urlpatterns = [
    #CUSTOMERS ENDPOINT
    path('customers/', customer_list_view),
    path('customer_detail/<int:pk>', customer_detail_view),

    #CURRENT ACCOUNT ENDPOINT
    path('current_accounts/', currentaccount_list_view),
    path('current_account_detail/<int:pk>', currentaccount_detail_view),

    #TRANSACTION ENDPOINT
    path('transactions/', transaction_list_view),
    path('transaction_detail/<int:pk>', transaction_detail_view),

]