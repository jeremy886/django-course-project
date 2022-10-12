from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
