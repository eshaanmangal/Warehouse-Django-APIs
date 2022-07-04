from django.db import models

from partners.models import Partner

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    measurement_units = models.CharField(max_length=5, default="kg")

class ProductTransaction(models.Model):
    DIRECTION = (
        ("IN", "in"),
        ("OUT", "out")
    )
    direction = models.CharField(max_length=5, choices=DIRECTION)
    name = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    partner_id = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, default=-1)

    def __str__(self):
        return '({0.direction!s}, {0.name!s}, {0.timestamp!s}, {0.amount!s})'.format(self)