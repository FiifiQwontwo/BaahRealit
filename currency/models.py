from django.db import models


# Create your models here.

class Currencies(models.Model):
    currency_code = models.CharField(max_length=4)
    currency_symbol = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency_symbol
