from django.contrib import admin
from django.urls import path
# from .views import *
from sms_app.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="index_page"),
    
]

