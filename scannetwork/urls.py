from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.nmap_view, name='nmap_view'),
]