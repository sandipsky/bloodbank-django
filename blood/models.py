from django.db import models
from users.models import *

class Stock(models.Model):
    bloodgroup=models.CharField(max_length=3)
    status=models.CharField(max_length=20, null=True)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    requester=models.ForeignKey(Hospital,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reason=models.CharField(max_length=500)
    bloodgroup=models.CharField(max_length=3)
    in_stock = models.BooleanField(null=True, default=True)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.bloodgroup
        
class BloodDonate(models.Model): 
    donor=models.ForeignKey(Donor,null=True,blank=True,on_delete=models.CASCADE)   
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.donor