from django.contrib import admin
# from sms_app.models import Student
from .models import Student
# Register your models here.

# admin.site.register(Student)  

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'age', 'phone']
    ordering = ['id']
