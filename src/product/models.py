from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    summary = models.TextField(
        max_length=128, default='this is a default value', blank=True, null=False)
    featured = models.BooleanField()
