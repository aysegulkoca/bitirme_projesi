from django.urls import path
from . import views

urlpatterns = [
    path('detail/<vulnerability>', views.cve_detail, name='cve_detail'),
]
