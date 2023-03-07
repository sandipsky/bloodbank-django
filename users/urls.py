from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from .views import *

urlpatterns = [
    # path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('donor/register/', donor_register_view, name='donor-register'),
    path('hospital/register/', hospital_register_view, name='hospital-register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('afterlogin/', afterlogin_view, name='after-login'),
    path('donor/dashboard/',donor_dashboard_view, name='donor-dashboard'),
    path('hospital/dashboard/', hospital_dashboard_view, name='hospital-dashboard')
]