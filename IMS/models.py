from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.IntegerField(blank=False, unique=True)
    product_name = models.CharField(max_length=100, blank=False)
    product_price = models.CharField( max_length=10,blank=False)
    product_discription = models.TextField()

    def __str__(self) :
        return self.product_name