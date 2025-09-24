from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class PaymentInfo(models.Model):
    payer_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    percent = models.PositiveSmallIntegerField()
    pay_date = models.DateTimeField()
