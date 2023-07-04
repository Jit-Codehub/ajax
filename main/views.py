from django.shortcuts import render
from .forms import StudentRegistration
from .models import *

def home(request):
    form = StudentRegistration()
    stu = Student.objects.all()
    return render(request, 'main/home.html', {'form':form,'stu':stu})
