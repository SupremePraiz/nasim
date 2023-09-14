from django.db import models
from django.contrib.auth.models import User

# Create your models here.


gender =(
    ('M','M'),('F','F')
)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="pics", default="default.png", null=True,blank=True)
    other_name = models.CharField(max_length=50,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(choices=gender, max_length=1,null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    state_of_origin = models.CharField(max_length=20,null=True)
    local_government_area_of_origin = models.CharField(max_length=70,null=True,blank=True)
    scheme_name = models.CharField(max_length=70,null=True,blank=True)
    year_of_application = models.DateField(null=True,blank=True)

    def __str__(self):
       return f"{self.other_name}"




    