from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_url = models.URLField(max_length=200, unique=True)
    product_img = models.URLField(max_length=200)
    product_nutriscore = models.CharField(max_length=10)
    product_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

class Nutriments(models.Model):
    nutriments_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    nutriments_kj = models.CharField(max_length=20)
    nutriments_kcal = models.CharField(max_length=20)
    nutriments_lipids = models.CharField(max_length=20)
    nutriments_fat = models.CharField(max_length=20)
    nutriments_carbohydrates = models.CharField(max_length=20)
    nutriments_sugar = models.CharField(max_length=20)
    nutriments_protein = models.CharField(max_length=20)
    nutriments_salt = models.CharField(max_length=20)
    nutriments_sodium = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=60)
    user_product = models.ManyToManyField(Product)

    def __str__(self):
        return self.username

