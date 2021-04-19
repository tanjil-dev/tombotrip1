from django.urls import path, re_path

from . import views
from .views import SupplyDetails,MessageDetailView,MessageListView,message_create

urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.test, name='test'),
    path('message/', views.test, name='message'),
    path('message/list',MessageListView.as_view(), name='message-list'),
    path('message/detail/<pk>',MessageDetailView.as_view(), name='message-list'),
    path('message_create/<str:username>',message_create, name='message-create'),
    path('details/<slug:slug>/',views.exp_details, name='exp-details' ),
    path('favourite/<int:id>/',views.favourite,name='favourite'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('supply/', views.supply, name='supply'),
    # path('reservation/', ReservationView.as_view(), name='reservation'),
    path('supply_details/<int:id>/<slug:slug>/',SupplyDetails.as_view(), name='supply-details' ),
    path('addcomment/<int:id>/',views.addcomment,name='addcomment'),
    path('filter-data',views.filter_data,name='filter_data'),
    # re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
]