from django.contrib import admin
from django.urls import path
# from .views import *
from sms_app.views import index_page, student_add, student_list

urlpatterns = [
    
    path('', index_page, name="index_page"),
    path('add/', student_add, name="student_add"),
    path('student_list/', student_list, name="student_list"),
    
]

