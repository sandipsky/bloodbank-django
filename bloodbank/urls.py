from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth.views import LogoutView,LoginView
from blood import views
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('users.urls')),
    path('', include('blood.urls')),
]