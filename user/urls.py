from django.urls import path

from home.views import ReservationView, UpdateReservationView, MyAdvertiseView, DeleteAdvertiseView, \
    UpdateAdvertiseView, AddAdvertiseView
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/reservation', ReservationView.as_view(), name='user_reservation'),
    path('my_advertise/', MyAdvertiseView.as_view(), name='my-advertise'),
    path('my_advertise/add', AddAdvertiseView.as_view(), name='add-advertise'),
    path('password/',views.user_password,name='password'),
    path('update/<str:pk>/', views.user_update,name='user_update'),
    path('profile/reservation/update/<str:pk>/', UpdateReservationView.as_view() ,name='update_user_reservation'),
    path('my_advertise/delete/<str:pk>/', DeleteAdvertiseView.as_view() ,name='delete-my-advertise'),
    path('my_advertise/update/<str:pk>/', UpdateAdvertiseView.as_view() ,name='update-my-advertise'),
    path('payment/<int:pk>/', views.stripePayment, name="payment"),
    path('payment/charge/<str:pk>/', views.charge, name="payment-charge"),
    path('payment/success/<str:args>/', views.successPayment, name="payment-success"),

  
    

]