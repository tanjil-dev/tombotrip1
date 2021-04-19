from django.urls import path

from home.views import ReservationView, UpdateReservationView
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/reservation', ReservationView.as_view(), name='user_reservation'),
    path('password/',views.user_password,name='password'),
    path('update/<str:pk>/', views.user_update,name='user_update'),
    path('profile/reservation/update/<str:pk>/', UpdateReservationView.as_view() ,name='update_user_reservation'),

  
    

]