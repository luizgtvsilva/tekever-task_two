from pickletools import read_long1
from itsdangerous import Serializer
from rest_framework import serializers
from task_two.serializers.serializer import *
from task_two.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name')


class CurrentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentAccount
        fields = ('id', 'customer_account', 'balance')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'from_customer', 'to_customer', 'amount', 'description')