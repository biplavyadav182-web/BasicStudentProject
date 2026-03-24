from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=255, default=True, null=True)
    
    