
from django.urls import path,include
from .views import *




urlpatterns = [
    path('daily-report/reports-list', get_end_of_day_reports,name='end_of_day_reports_list' ),
    path('daily-report/morning-reports-list', get_morning_reports,name='morning_reports_list' ),
    path('daily-report/today', get_full_report_by_date,name='full_report' )
    # path('daily-report/morning-reports-list/<int:year>/<int:month>/<int:day>', get_morning_reports_by_date,name='morning_reports_list' )
    
]
