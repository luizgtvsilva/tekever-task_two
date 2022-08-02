from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)    


class CurrentAccount(models.Model):
    customer_account = models.IntegerField(unique=True, blank=False, null=False)
    balance = models.FloatField()
    

class Transaction(models.Model):
    from_customer = models.IntegerField(blank=False, null=False)
    to_customer = models.IntegerField(blank=False, null=False)
    amount = models.FloatField()
    description = models.CharField(max_length=300)
