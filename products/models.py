from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    body = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"{self.category.name}  {self.model}"


