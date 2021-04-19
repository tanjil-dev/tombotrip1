from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog,name='blog'),
    path('<slug:slug>/',views.blogdetails, name='post-detail' ),
    path("category/<slug:slug>/posts", views.Posts_in_CategoryView, name="posts_in_category"),
   
    
]
