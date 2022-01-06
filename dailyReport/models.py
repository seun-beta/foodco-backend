from django.db import models

# Create your models here.

TIME_OF_DAY =  (
        ('Morning','Morning'),
        ('Evening','Evening'),
        
    )


class RawMaterial(models.Models):
    material = models.CharField(unique=True,max_length=255)
    price = models.FloatField()
    transfer_cost = models.FloatField()
    recipe_cost = models.FloatField()
    
    
    def __str__(self) -> str:
        return self.material
    
    

class Product(models.Model):
    product = models.CharField()
    quantity = models.IntegerField()
    transfer_price = models.FloatField()
    value = models.FloatField()
    
    
    
    def __str__(self) -> str:
        return self.product
    
    
    
    
class MorningEntry(models.Model):
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    created_by = models.CharField()
    time_of_day =models.CharField(choices=TIME_OF_DAY)
    created_at= models.DateTimeField( auto_now=False, auto_now_add=True)
    
    
    
    
class EveningEntry(models.Model):
    
    created_by = models.CharField()
    time_of_day =models.CharField(choices=TIME_OF_DAY)
    created_at= models.DateTimeField( auto_now=False, auto_now_add=True)
    