from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from .views import *

urlpatterns = [

    #ADMIN
    path('', admin_dashboard_view,name='admin-dashboard'),
    path('bloodstock/', blood_stock_view,name='blood-stock'),
    path('bloodstock/add/',blood_stock_add,name='blood-stock-add'),
    path('bloodstock/edit/<int:pk>', blood_stock_edit,name='blood-stock-edit'),
    path('bloodstock/delete/<int:pk>', blood_stock_delete,name='blood-stock-delete'),
    path('donors/', donor_view, name='donors'),
    path('donors/add/', donor_add, name='donor-add'),
    path('donors/edit/<int:pk>', donor_edit, name='donor-edit'),
    path('donors/delete/<int:pk>', donor_delete, name='donor-delete'),

    #DONOR


    #HOSPITAL
]