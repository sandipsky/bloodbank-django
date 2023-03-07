from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.
def logout_view(request):
  logout(request)

# def donor_signup_view(request):
#     userForm=forms.DonorUserForm()
#     donorForm=forms.DonorForm()
#     mydict={'userForm':userForm,'donorForm':donorForm}
#     if request.method=='POST':
#         userForm=forms.DonorUserForm(request.POST)
#         donorForm=forms.DonorForm(request.POST,request.FILES)
#         if userForm.is_valid() and donorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             donor=donorForm.save(commit=False)
#             donor.user=user
#             donor.bloodgroup=donorForm.cleaned_data['bloodgroup']
#             donor.save()
#             my_donor_group = Group.objects.get_or_create(name='DONOR')
#             my_donor_group[0].user_set.add(user)
#         return HttpResponseRedirect('donorlogin')
#     return render(request,'donor/donorsignup.html',context=mydict)




# def patient_signup_view(request):
#     userForm=forms.PatientUserForm()
#     patientForm=forms.PatientForm()
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST)
#         patientForm=forms.PatientForm(request.POST,request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.bloodgroup=patientForm.cleaned_data['bloodgroup']
#             patient.save()
#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)
#         return HttpResponseRedirect('patientlogin')
#     return render(request,'patient/patientsignup.html',context=mydict)


