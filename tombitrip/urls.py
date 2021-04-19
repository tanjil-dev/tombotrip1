
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import search
from home import views as homeviews
# local
from user import views as userviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('blog/',include("blog.urls")),
    path('user/',include("user.urls")),
  
    path('contact/',include("contact.urls")),
    path('listvehicle/',include("listvehicle.urls")),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    


    # local 
    path('search/',search,name='search'),
    path('supplysearch/',homeviews.supplysearch,name='supplysearch'),
    path('signup/',userviews.signup_form, name='signup_form'),
    path('login/',userviews.login_form, name='login_form'),
    path('logout/',userviews.logout_func, name='logout'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
