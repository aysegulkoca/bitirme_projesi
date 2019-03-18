from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_new, name='report_new'),
    path('list/', views.report_list, name='report_list'),
    path('detail/<int:pk>/', views.report_detail, name='report_detail'),
    path('<int:pk>/delete', views.report_delete, name='report_delete'),
]
