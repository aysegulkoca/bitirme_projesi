from django.conf.urls import url
from .views import *

app_name = 'authentication'

urlpatterns = [

   url(r'^login/$', login_view, name='login_view'),

]
