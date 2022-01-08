import datetime
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.serializers import Serializer
from .serializers import *
from .models import *
import datetime
# Create your views here.


@api_view(['POST'])
def end_of_day_report(request):
    
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
    
    # results = RawMaterialRecieved.objects.raw('SELECT * FROM dailyReports_ GROUP BY date')
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
def get_full_report_by_date(request):
    morning_report = RawMaterialRecieved.objects.filter(date=datetime.datetime.today())
    evening_report = EndOfDayReport.objects.get(date=datetime.datetime.today())
    morning_reportSerializer = RawMaterialsRecievedSerializer(morning_report,many=True)
    end_of_day_reportSerializer = EndOfDayReportSerializer(evening_report)
    response = Response()
    response.data = {
        'status':200,
        'data':[ {'raw_materials':morning_reportSerializer.data, 'report':end_of_day_reportSerializer.data}]
    }
    return response