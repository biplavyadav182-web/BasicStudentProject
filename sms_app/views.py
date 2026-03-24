from django.shortcuts import render
# from sms_app.models import Student
from .models import Student

# Create your views here.
def index_page(request):
    return render(request, "main/index.html")

def student_add(request):
    #Receive data in dictionary (storing in container)
    if request.method == "POST":
            
            data = request.POST
            
            fn = data["firstname"]
            ln = data["lastname"]
            age = data["age"]
            phone = data["phone"]
            email = data["email"]
            comments =data["mssg"]
        
            student_data = Student(first_name=fn, last_name=ln, age=age, phone=phone, email=email, message=comments)
            student_data.save()       
                
    return render(request, "main/AddStudent.html")