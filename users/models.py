from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=3)
    dob=models.DateField()
    location = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, unique=True)
    disease = models.CharField(max_length=100,default="none")
    email = models.CharField(max_length=100, unique=True)
    eligibility = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.user.username
        
        
class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=100, null=True)
    identification = models.CharField(max_length=200)
   
    def __str__(self):
        return self.user.username