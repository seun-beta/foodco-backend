from django.db.models import fields
from rest_framework import response, serializers, status


from .models import RawMaterialRecieved,EndOfDayReport,MorningEntry,Disribution,Pastry


class RawMaterialsRecievedSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = RawMaterialRecieved
        fields =  '__all__'
                  
                  
class PostRawMaterialsRecievedSerializer(serializers.ModelSerializer):
    
    
    # def create(self, request, *args, **kwargs):
    #     many = True if isinstance(request.data, list) else False

    #     serializer = self.get_serializer(data=request.data, many=many)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return response.Response(serializer.data, status=status.HTTP_201_CREATED,)
    
    class Meta:
        model = RawMaterialRecieved
        fields =  [
            "pastry",
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
        
class PastrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pastry
        fields = '__all__'
        
class DistributionSerializer(serializers.ModelSerializer):
    pastry = PastrySerializer()
    class Meta:
        model = Disribution
        fields = ['cost_of_distribution','branch','pastry']






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
        

class PostEndOfDayReportSerializer(serializers.ModelSerializer):
    distribution = DistributionSerializer(many=True)
    
    
    # distribution_id = EndOfDayReport.objects.get(id)
    class Meta:
        model = EndOfDayReport
        fields =[
            
             'no_of_pastries',
    'no_of_pastries_sent',
    'no_of_pastries_not_sold',
    'distribution'     ,'date'   ]
    
    
    def create(self, validated_data):
        distributions_data = validated_data.pop('distribution')
        report = EndOfDayReport.objects.create(**validated_data)
        for distribution_data in distributions_data:
            Disribution.objects.create(report=report, **distribution_data)
        return report
    # def get_distribution(self,):s