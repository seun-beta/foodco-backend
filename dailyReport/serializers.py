from django.db.models import fields
from rest_framework import serializers


from .models import RawMaterialRecieved,EndOfDayReport,MorningEntry,Disribution,Pastries


class RawMaterialsRecievedSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = RawMaterialRecieved
        fields =  '__all__'
                  
                  
class PostRawMaterialsRecievedSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = RawMaterialRecieved
        fields =  [
            
                "material",
    "amount",
    "price",
    "transfer_cost",
    "material_cost"
            
        ]
                  
                  
        
class MorningEntry(serializers.ModelSerializer):
    
    
    class Meta:
        model = MorningEntry
        fields = [
              'raw_material',
    'created_by',
    'time_of_day'
            
            
        ]
        
        
class DistributionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Disribution
        fields = ['cost_of_distribution','branch']






class EndOfDayReportSerializer(serializers.ModelSerializer):
    distribution = DistributionSerializer()
    
    
    # distribution_id = EndOfDayReport.objects.get(id)
    class Meta:
        model = EndOfDayReport
        fields =[
            
             'no_of_pastries',
    'no_of_pastries_sent',
    'no_of_pastries_not_sold',
    'distribution'     ,'date'   ]
        
    # def get_distribution(self,):s