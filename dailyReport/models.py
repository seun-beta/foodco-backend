from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

# Create your models here.

TIME_OF_DAY =  (
        ('Morning','Morning'),
        ('Evening','Evening'),
        
    )

RAW_MATERIALS = (
('sugar','Sugar'),
('salt','Salt'),
('Flour','Flour')
)

PRODUCTS_PRODUCED = (
    
    
    ('meat_pie','Meat Pie'),
    ('chicken_pie','Chicken Pie'),
    ('doughnut','Doughnut')
)
BRANCH = (
    
    
    ('jericho','Jericho'),
    ('ring_road','Ring Road'),
    ('bodija','Bodija')
)



    

class RawMaterialRecieved(models.Model):
    material = models.CharField(choices=RAW_MATERIALS,max_length=255)
    amount=models.FloatField() #in grams
    price = models.FloatField() 
    transfer_cost = models.FloatField()
    material_cost = models.FloatField()
    date = models.DateField(verbose_name="date", auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.material
    
    
    
    
class MorningEntry(models.Model):
    raw_material = models.ForeignKey(RawMaterialRecieved, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=255)
    time_of_day =models.CharField(choices=TIME_OF_DAY,max_length=255)
    date = models.DateField(auto_now_add=True)
    created_at= models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.raw_material}---{self.date}"
    
    
    
    
    
    
    
class Disribution(models.Model):
    cost_of_distribution = models.FloatField()
    branch = models.CharField(max_length=255,choices=BRANCH,default='Jericho')
    date = models.DateField( auto_now=False, auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"Distrobution for {self.branch} on {self.date}"
    
    
    
    
class EndOfDayReport(models.Model):
    no_of_pastries = models.IntegerField()
    no_of_pastries_sent = models.IntegerField()
    no_of_pastries_not_sold = models.IntegerField()
    distribution = models.ForeignKey(Disribution,on_delete=CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return f" End of Day Report for {self.date}"
    
  
  
  
    
class Pastries(models.Model):
    product = models.CharField(max_length=255,choices=PRODUCTS_PRODUCED)
    quantity = models.IntegerField()
    price = models.FloatField()
    # use quantity and price to calculate total price of all pastries made in a day