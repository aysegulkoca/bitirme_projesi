from django.conf.urls import url
from .views import *

app_name = 'scanweb'

urlpatterns = [

   url(r'^web/$', scan_web, name='scan_web'),

]
