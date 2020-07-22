from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    product_url = models.URLField(max_length=200, unique=True)
    product_img = models.URLField(max_length=200, unique=True)
    product_nutriscore = models.CharField(max_length=1)
    

class Nutriments(models.Model):
    nutriments_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    nutriments_kj = models.CharField(max_length=10)
    nutriments_kcal = models.CharField(max_length=10)
    nutriments_lipids = models.CharField(max_length=10)
    nutriments_fat = models.CharField(max_length=10)
    nutriments_carbohydrates = models.CharField(max_length=10)
    nutriments_sugar = models.CharField(max_length=10)
    nutriments_protein = models.CharField(max_length=10)
    nutriments_salt = models.CharField(max_length=10)
    nutriments_sodium = models.CharField(max_length=10)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_mail = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=60)
    user_product = models.ManyToManyField(Product, related_name='product', blank=True)

