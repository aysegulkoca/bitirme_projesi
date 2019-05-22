from django.urls import path
from . import views

urlpatterns = [

   path('web/', views.scan_web, name='scan_web'),
   path('web/detail/<int:pk>/', views.web_report_detail, name='scanweb_detail_list'),
   path('weblist/', views.web_report_list, name='scanweb_report_list'),

]
