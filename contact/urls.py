from django.urls import path

from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('traveller/', views.traveller, name='traveller'),
    path('ownercamper/', views.ownercamper, name='ownercamper'),
    path('ownercaravan/', views.ownercaravan, name='ownercaravan'),


]