from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Sum,Q
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models.functions import ExtractDay

# Create your views here.

#Admin

# def is_donor(user):
#returns boolean value
#     return user.groups.filter(name='DONOR').exists()

# def is_patient(user):
#     return user.groups.filter(name='PATIENT').exists()


# def afterlogin_view(request):
#     if is_donor(request.user):      
#         return redirect('donor/donor-dashboard')
                
#     elif is_patient(request.user):
#         return redirect('patient/patient-dashboard')
#     else:
#         return redirect('admin-dashboard')

# @login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={

        # 'totaldonors':dmodels.Donor.objects.all().count(),
        'bloods': Stock.objects.all(), 
        'totalbloodunit':totalunit['unit__sum'],
        #'totalrequest':models.BloodRequest.objects.all().count(),
        #'totalapprovedrequest':models.BloodRequest.objects.all().filter(status='Approved').count()
    }
    return render(request,'admin_dashboard.html',context=dict)

def blood_stock_view(request):
    dict={
        'bloods': Stock.objects.all(), 
    }
    return render(request,'stock.html',context=dict)

def blood_stock_add_view(request):
    form=BloodForm(request.POST)
    if request.method=='POST':
        form=BloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
        else:
            form = BloodForm()
    context = {'form':form}
    return render(request,'stock_add.html',context)

def blood_stock_edit_view(request, pk):
    item = Stock.objects.get(id=pk)
    form=BloodForm(instance=item)
    if request.method=='POST':
        form=BloodForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')  
    context = {'form':form, 'item':item}
    return render(request,'stock_edit.html',context)

def blood_stock_delete(request, pk):
    item = Stock.objects.get(id=pk)
    item.delete()
    return redirect('/bloodstock')


def make_request_view(request):
    request_form=RequestForm()
    if request.method=='POST':
        request_form=RequestForm(request.POST)
        if request_form.is_valid():
            bloodgroup=request_form.cleaned_data['bloodgroup']
            unit=request_form.cleaned_data['unit']
            stock=models.Stock.objects.get(bloodgroup=bloodgroup)
            if stock.unit < unit:
                request_form.instance.in_stock = False

                #send email 
            request_form.save()
            return redirect('/bloodstock')  
    return render(request,'request.html',{'request_form':request_form})

def admin_request_view(request):
    # requests=models.BloodRequest.objects.all().filter(status='Pending')
    requests=BloodRequest.objects.all()
    req = BloodRequest.objects.last()
    current_date = date.today()
    date1 = date(2023, 3, 5)
    # diff = current_date - req.date
    diff = current_date - date1
    day = diff.days
    return render(request,'bloodrequest.html',{'requests':requests, 'day': day})

def request_view(request):
    requests=BloodRequest.objects.all().filter(in_stock=False)
    return render(request,'nostock.html',{'requests':requests})

# @login_required(login_url='adminlogin')
# def admin_blood_view(request):
#     dict={
#         'bloodForm':forms.BloodForm(),
#         'A1':models.Stock.objects.get(bloodgroup="A+"),
#         'A2':models.Stock.objects.get(bloodgroup="A-"),
#         'B1':models.Stock.objects.get(bloodgroup="B+"),
#         'B2':models.Stock.objects.get(bloodgroup="B-"),
#         'AB1':models.Stock.objects.get(bloodgroup="AB+"),
#         'AB2':models.Stock.objects.get(bloodgroup="AB-"),
#         'O1':models.Stock.objects.get(bloodgroup="O+"),
#         'O2':models.Stock.objects.get(bloodgroup="O-"),
#     }
#     if request.method=='POST':
#         bloodForm=forms.BloodForm(request.POST)
#         if bloodForm.is_valid() :        
#             bloodgroup=bloodForm.cleaned_data['bloodgroup']
#             stock=models.Stock.objects.get(bloodgroup=bloodgroup)
#             stock.unit=bloodForm.cleaned_data['unit']
#             stock.save()
#         return HttpResponseRedirect('admin-blood')
#     return render(request,'blood/admin_blood.html',context=dict)


# @login_required(login_url='adminlogin')
# def admin_donor_view(request):
#     donors=dmodels.Donor.objects.all()
#     return render(request,'blood/admin_donor.html',{'donors':donors})

# @login_required(login_url='adminlogin')
# def update_donor_view(request,pk):
#     donor=dmodels.Donor.objects.get(id=pk)
#     user=dmodels.User.objects.get(id=donor.user_id)
#     userForm=dforms.DonorUserForm(instance=user)
#     donorForm=dforms.DonorForm(request.FILES,instance=donor)
#     mydict={'userForm':userForm,'donorForm':donorForm}
#     if request.method=='POST':
#         userForm=dforms.DonorUserForm(request.POST,instance=user)
#         donorForm=dforms.DonorForm(request.POST,request.FILES,instance=donor)
#         if userForm.is_valid() and donorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             donor=donorForm.save(commit=False)
#             donor.user=user
#             donor.bloodgroup=donorForm.cleaned_data['bloodgroup']
#             donor.save()
#             return redirect('admin-donor')
#     return render(request,'blood/update_donor.html',context=mydict)


# @login_required(login_url='adminlogin')
# def delete_donor_view(request,pk):
#     donor=dmodels.Donor.objects.get(id=pk)
#     user=User.objects.get(id=donor.user_id)
#     user.delete()
#     donor.delete()
#     return HttpResponseRedirect('/admin-donor')

# @login_required(login_url='adminlogin')
# def admin_patient_view(request):
#     patients=pmodels.Patient.objects.all()
#     return render(request,'blood/admin_patient.html',{'patients':patients})


# @login_required(login_url='adminlogin')
# def update_patient_view(request,pk):
#     patient=pmodels.Patient.objects.get(id=pk)
#     user=pmodels.User.objects.get(id=patient.user_id)
#     userForm=pforms.PatientUserForm(instance=user)
#     patientForm=pforms.PatientForm(request.FILES,instance=patient)
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=pforms.PatientUserForm(request.POST,instance=user)
#         patientForm=pforms.PatientForm(request.POST,request.FILES,instance=patient)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.bloodgroup=patientForm.cleaned_data['bloodgroup']
#             patient.save()
#             return redirect('admin-patient')
#     return render(request,'blood/update_patient.html',context=mydict)


# @login_required(login_url='adminlogin')
# def delete_patient_view(request,pk):
#     patient=pmodels.Patient.objects.get(id=pk)
#     user=User.objects.get(id=patient.user_id)
#     user.delete()
#     patient.delete()
#     return HttpResponseRedirect('/admin-patient')

# @login_required(login_url='adminlogin')
# def admin_request_view(request):
#     requests=models.BloodRequest.objects.all().filter(status='Pending')
#     return render(request,'blood/admin_request.html',{'requests':requests})

# @login_required(login_url='adminlogin')
# def admin_request_history_view(request):
#     requests=models.BloodRequest.objects.all().exclude(status='Pending')
#     return render(request,'blood/admin_request_history.html',{'requests':requests})

# @login_required(login_url='adminlogin')
# def admin_donation_view(request):
#     donations=dmodels.BloodDonate.objects.all()
#     return render(request,'blood/admin_donation.html',{'donations':donations})

# @login_required(login_url='adminlogin')
# def update_approve_status_view(request,pk):
#     req=models.BloodRequest.objects.get(id=pk)
#     message=None
#     bloodgroup=req.bloodgroup
#     unit=req.unit
#     stock=models.Stock.objects.get(bloodgroup=bloodgroup)
#     if stock.unit >= unit:
#         stock.unit=stock.unit-unit
#         stock.save()
#         req.status="Approved"
        
#     else:
#         message="Stock Doest Not Have Enough Blood To Approve This Request, Only "+str(stock.unit)+" Unit Available"
#     req.save()

#     requests=models.BloodRequest.objects.all().filter(status='Pending')
#     return render(request,'blood/admin_request.html',{'requests':requests,'message':message})

# @login_required(login_url='adminlogin')
# def update_reject_status_view(request,pk):
#     req=models.BloodRequest.objects.get(id=pk)
#     req.status="Rejected"
#     req.save()
#     return HttpResponseRedirect('/admin-request')

# @login_required(login_url='adminlogin')
# def approve_donation_view(request,pk):
#     donation=dmodels.BloodDonate.objects.get(id=pk)
#     donation_blood_group=donation.bloodgroup
#     donation_blood_unit=donation.unit

#     stock=models.Stock.objects.get(bloodgroup=donation_blood_group)
#     stock.unit=stock.unit+donation_blood_unit
#     stock.save()

#     donation.status='Approved'
#     donation.save()
#     return HttpResponseRedirect('/admin-donation')


# @login_required(login_url='adminlogin')
# def reject_donation_view(request,pk):
#     donation=dmodels.BloodDonate.objects.get(id=pk)
#     donation.status='Rejected'
#     donation.save()
#     return HttpResponseRedirect('/admin-donation')


#Donor

# def donor_dashboard_view(request):
#     donor= models.Donor.objects.get(user_id=request.user.id)
#     dict={
#         'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Pending').count(),
#         'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Approved').count(),
#         'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).count(),
#         'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Rejected').count(),
#     }
#     return render(request,'donor/donor_dashboard.html',context=dict)


# def donate_blood_view(request):
#     donation_form=forms.DonationForm()
#     if request.method=='POST':
#         donation_form=forms.DonationForm(request.POST)
#         if donation_form.is_valid():
#             blood_donate=donation_form.save(commit=False)
#             blood_donate.bloodgroup=donation_form.cleaned_data['bloodgroup']
#             donor= models.Donor.objects.get(user_id=request.user.id)
#             blood_donate.donor=donor
#             blood_donate.save()
#             return HttpResponseRedirect('donation-history')  
#     return render(request,'donor/donate_blood.html',{'donation_form':donation_form})

# def donation_history_view(request):
#     donor= models.Donor.objects.get(user_id=request.user.id)
#     donations=models.BloodDonate.objects.all().filter(donor=donor)
#     return render(request,'donor/donation_history.html',{'donations':donations})

# def make_request_view(request):
#     request_form=bforms.RequestForm()
#     if request.method=='POST':
#         request_form=bforms.RequestForm(request.POST)
#         if request_form.is_valid():
#             blood_request=request_form.save(commit=False)
#             blood_request.bloodgroup=request_form.cleaned_data['bloodgroup']
#             donor= models.Donor.objects.get(user_id=request.user.id)
#             blood_request.request_by_donor=donor
#             blood_request.save()
#             return HttpResponseRedirect('request-history')  
#     return render(request,'donor/makerequest.html',{'request_form':request_form})

# def request_history_view(request):
#     donor= models.Donor.objects.get(user_id=request.user.id)
#     blood_request=bmodels.BloodRequest.objects.all().filter(request_by_donor=donor)
#     return render(request,'donor/request_history.html',{'blood_request':blood_request})





#Patient
# def patient_dashboard_view(request):
#     patient= models.Patient.objects.get(user_id=request.user.id)
#     dict={
#         'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Pending').count(),
#         'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Approved').count(),
#         'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).count(),
#         'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Rejected').count(),

#     }
   
#     return render(request,'patient/patient_dashboard.html',context=dict)



# def my_request_view(request):
#     patient= models.Patient.objects.get(user_id=request.user.id)
#     blood_request=bmodels.BloodRequest.objects.all().filter(request_by_patient=patient)
#     return render(request,'patient/my_request.html',{'blood_request':blood_request})