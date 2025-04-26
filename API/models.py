from django.db import models

# Create your models here.
class Item(models.Model):
    name1 = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    barcode = models.IntegerField(unique = True)
