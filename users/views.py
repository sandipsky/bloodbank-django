from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import *

# Create your views here.
def donor_register_view(request):
    userForm=UserForm()
    donorForm=DonorForm()
    mydict={'userForm':userForm,'donorForm':donorForm}
    if request.method=='POST':
        userForm=UserForm(request.POST)
        donorForm=DonorForm(request.POST)
        if userForm.is_valid() and donorForm.is_valid():
            user=userForm.save()
            user.save()
            donor=donorForm.save(commit=False)
            donor.user=user
            donor.bloodgroup=donorForm.cleaned_data['bloodgroup']
            donor.save()
            donor_group = Group.objects.get_or_create(name='DONOR')
            donor_group[0].user_set.add(user)
            return redirect('login')
        
    return render(request,'donor/registerdonor.html',context=mydict)

def hospital_register_view(request):
    userForm=UserForm()
    hospitalForm=HospitalForm()
    mydict={'userForm':userForm,'hospitalForm':hospitalForm}
    if request.method=='POST':
        userForm=UserForm(request.POST)
        hospitalForm=HospitalForm(request.POST,request.FILES)
        if userForm.is_valid() and hospitalForm.is_valid():
            user=userForm.save()
            user.save()
            hospital=hospitalForm.save(commit=False)
            hospital.user=user
            hospital.save()
            hospital_group = Group.objects.get_or_create(name='HOSPITAL')
            hospital_group[0].user_set.add(user)
            return redirect('login')
        
    return render(request,'hospital/registerhospital.html',context=mydict)

def logout_user(request):
  logout(request)
  return redirect('login')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('after-login')
        elif not User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'User not found'})
        else:
            return render(request, 'login.html', {'error': 'Username or Password is Incorrect'})
    return render(request, 'login.html')


def is_donor(user):
    return user.groups.filter(name='DONOR').exists()

def is_hospital(user):
    return user.groups.filter(name='HOSPITAL').exists()

def afterlogin_view(request):
    if is_donor(request.user):      
        return redirect('donor-dashboard')
                
    if is_hospital(request.user):
        return redirect('hospital-dashboard')
    
    else:
        return redirect('admin-dashboard')

def donor_dashboard_view(request):
    return render(request, 'donor/donordashboard.html')

def hospital_dashboard_view(request):
    return render(request, 'hospital/hospitaldashboard.html')







