
from django.urls import path,include
from .views import *




urlpatterns = [
    path('daily-report/reports-list', get_end_of_day_reports,name='end_of_day_reports_list' ),
    path('daily-report/add-end-of-day-report', post_end_of_day_report,name='post_end_of_day_report' ),
    path('daily-report/enter-material', post_raw_material,name='fill_report' ),
    path('daily-report/report/<str:date>', get_full_report_by_date,name='full_report' ),
    path('daily-report/get-branches', get_branch_list,name='get_branches' ),
    path('daily-report/get-materials', get_materials_list,name='get_materials' ),
    path('daily-report/get-products', get_products_list,name='get_products' ),
    
    # im thinking of how we can get a list of reports by date, so the FE can make a list through that, and allow users to select by date. Filter is there, i just need to ensure that the date entered is not out of scope
    
]
