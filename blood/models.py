from django.db import models
from users.models import *
from datetime import date


class Stock(models.Model):
    bloodgroup=models.CharField(max_length=3,)
    date=models.DateField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.bloodgroup
    
    @property
    def isActive(self):
        current_date = date.today()
        diff = current_date - self.date
        day = diff.days
        if day > 30:
            return False
        else:
            return True

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