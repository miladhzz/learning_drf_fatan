from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_code = models.IntegerField()
    about_product = models.CharField(max_length=200)
    image_product = models.ImageField()
    price = models.IntegerField()
    count = models.IntegerField()
    Product_type = (
        ("bs1", "BS1"),
        ("bs2", "BS2"),
        ("bs3", "BS3"),
        ("bb1", "BB1"),
        ("bb2", "BB2"),
        ("bb3", "BB3"),
    )
    product_type = models.CharField(max_length=10, choices=Product_type)

