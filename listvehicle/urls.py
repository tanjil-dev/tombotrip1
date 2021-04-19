from django.urls import path

from . import views

urlpatterns = [
    path('listvehicle/', views.listvehicle, name='listvehicle'),
    path('agents/', views.agents, name='agents'),
    
    
]