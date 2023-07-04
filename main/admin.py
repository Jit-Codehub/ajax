from django.contrib import admin
from . models import *

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudenetAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']