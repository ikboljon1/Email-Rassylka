from django.urls import path 
from emailapp import views 

urlpatterns = [ 
    path('', views.home_view, name='subscribers'), 
]