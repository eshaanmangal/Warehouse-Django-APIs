from django.db import models

from partners.models import Partner

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    measurement_units = models.CharField(max_length=5, default="kg")

class ProductTransaction(models.Model):
    DIRECTION = (
        ("IN", "in"),
        ("OUT", "out")
    )
    direction = models.CharField(max_length=5, choices=DIRECTION)
    name = models.CharField(max_length=60)
    timestamp = models.DateTimeField()
    product_id_type = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    partner_id = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, default=-1)