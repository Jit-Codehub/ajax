from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistration
from .models import *

def home(request):
    form = StudentRegistration()
    stu = Student.objects.all()
    return render(request, 'main/home.html', {'form':form,'stu':stu})

def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            Student.objects.create(name=name, email=email, password=password)
            stud = Student.objects.values()
            student_data = list(stud)
            return JsonResponse({"status":200, "student_data":student_data})
        else:
            return JsonResponse({"status":0})
        
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        Student.objects.get(pk=id).delete()
        return JsonResponse({"status":200})
    else:
        return JsonResponse({"status":0})

