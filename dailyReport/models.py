from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

# Create your models here.

TIME_OF_DAY =  (
        ('Morning','Morning'),
        ('Evening','Evening'),
        
    )

RAW_MATERIALS = (
('Flour','Flour')
('Flour','Flour')
('Flour','Flour')
('Flour','Flour')
('Flour','Flour')
('Flour','Flour')
)

PRODUCTS_PRODUCED = (
    
    
    
    ('meat_pie','Meat Pie')
    ('meat_pie','Meat Pie')
    ('meat_pie','Meat Pie')
    ('meat_pie','Meat Pie')
    ('meat_pie','Meat Pie')
)



    

class RawMaterialRecieved(models.Models):
    material = models.CharField(choices=RAW_MATERIALS,max_length=255)
    amount=models.FloatField() #in grams
    price = models.FloatField() 
    transfer_cost = models.FloatField()
    material_cost = models.FloatField()
    time_of_day = models.DateField(verbose_name="date", auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.material
    
    
    
    
class MorningEntry(models.Model):
    raw_material = models.ForeignKey(RawMaterialRecieved, on_delete=models.CASCADE)
    created_by = models.CharField()
    time_of_day =models.CharField(choices=TIME_OF_DAY)
    date = models.DateField(auto_now_add=True)
    created_at= models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.raw_material}---{self.date}"
    
    
    
    
    
    
    
class Disribution(models.Model):
    cost_of_distribution = models.FloatField()
    
    
    
    
class EndOfDayReport(models.Model):
    no_of_pastries = models.IntegerField()
    no_of_pastries_sent = models.IntegerField()
    no_of_pastries_not_sold = models.IntegerField()
    distribution = models.OneToOneField(Disribution,on_delete=CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return f" End of Day Report for ---{self.date}"
    
  
  
  
    
class Pastries(models.Model):
    product = models.CharField(choices=PRODUCTS_PRODUCED)
    quantity = models.IntegerField()
    price = models.FloatField()
    # use quantity and price to calculate total price of all pastries made in a day