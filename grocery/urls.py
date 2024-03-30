from django.urls import path
from grocery.views import *

urlpatterns = [
    path('atta/',atta,name='atta'),
   
]