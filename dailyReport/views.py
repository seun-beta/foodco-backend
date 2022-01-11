import datetime
from django.shortcuts import render
from rest_framework import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.serializers import Serializer
from .serializers import *
from .models import *
import datetime
# Create your views here.
@api_view(['GET'])
def get_branch_list(request):
    return Response(data= ['Jericho',
    'Ring Road',
    'Bodija'
])
@api_view(['GET'])
def get_materials_list(request):
    return Response(data= 
                    ['sugar',
    'salt',
    'flour',
    'butter',
])
@api_view(['GET'])
def get_products_list(request):
    return Response(data= 
                    [
                        'Meat Pie',
    'Chicken Pie',
    'Doughnut'
    'Sussage'
])

@api_view(['POST'])
def post_end_of_day_report(request):
    
    data = request.data 
    serializer = EndOfDayReportSerializer(data)
    if serializer.is_valid():
        serializer.save()
        response = Response()
        response.data = {
            'status':201,
            'message':'Entry Successful',
            'report':serializer.data
        }
        return response
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET'])
def get_end_of_day_reports(request):
    
    reports =  EndOfDayReport.objects.all()
    # distribution = Disribution.objects.get(id=reports[0]['distribution'])
    # distributionSerializer = EndOfDayReportSerializer(distribution)
    serializer = EndOfDayReportSerializer(reports,many= True)
    if request.method == 'GET':
        response = Response()
        response.data = {
            'status':200,
            'reports':serializer.data,
            # 'distribution':distributionSerializer.data
        }
        return response
    
    
    
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        
        
@api_view(['GET'])    
def daily_distribution(request):
    data =request.data
    
    serializer = DistributionSerializer(data)
    if serializer :
        serializer.save()
    
    return Response( status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def post_raw_material(request):
    data = JSONParser().parse(request)
    serializer = PostRawMaterialsRecievedSerializer(data=data,many = True)
    response = Response()
    date = datetime.datetime.today()    
    for obj in data:
        material = obj['material']
        if not RawMaterialRecieved.objects.filter(date=date).filter(material=material).exists():
            serializer = PostRawMaterialsRecievedSerializer(data=data,many= True)
            if serializer.is_valid():
                serializer.save()
                print(data)
                response.data = { "data":serializer.data, "status":status.HTTP_201_CREATED,}
                return response

                return Response(data=serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    return Response(data={'status':status.HTTP_400_BAD_REQUEST,'message':'Data already exists'})





@api_view(['GET'])
def post_end_of_day_report(request):
    response = Response()
    
    
    return response


@api_view(['GET'])
def get_morning_reports(request):
    
    # results = RawMaterialRecieved.objects.raw('SELECT * FROM dailyReports_ GROUP BY date')
    report = RawMaterialRecieved.objects.all()
    report_serializer = RawMaterialsRecievedSerializer(report,many=True)
    if report_serializer :
        response = Response()
        response.data = {
            
            'status':200,
            'report':report_serializer.data
        }
        return response
    
    
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_morning_reports_by_date(request,date):
    report = RawMaterialRecieved.objects.filter(date=date)
    report_serializer = RawMaterialsRecievedSerializer(report,many=True)
    if report_serializer :
        response = Response()
        response.data = {
            
            'status':200,
            'report':report_serializer.data
        }
        return response
    
    
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_full_report_by_date(request,date):
    morning_report = RawMaterialRecieved.objects.filter(date=date)
    evening_report = EndOfDayReport.objects.get(date=date)
    morning_reportSerializer = RawMaterialsRecievedSerializer(morning_report,many=True)
    end_of_day_reportSerializer = EndOfDayReportSerializer(evening_report)
    response = Response()
    response.data = {
        'status':200,
        'data':[ {'raw_materials':morning_reportSerializer.data, 'report':end_of_day_reportSerializer.data}]
    }
    return response

@api_view(['GET'])
def get_end_of_day_report_by_date(request,date):
    evening_report = EndOfDayReport.objects.get(date=date)
    end_of_day_reportSerializer = EndOfDayReportSerializer(evening_report)
    response = Response()
    response.data = {
        'status':200,
        'data':[ {'report':end_of_day_reportSerializer.data}]
    }
    return response


@api_view(['GET'])
def get_full_materials_by_date(request,date):
    morning_report = RawMaterialRecieved.objects.filter(date=date)
    morning_reportSerializer = RawMaterialsRecievedSerializer(morning_report,many=True)
    response = Response()
    response.data = {
        'status':200,
        'data':[ {'raw_materials':morning_reportSerializer.data}]
    }
    return response