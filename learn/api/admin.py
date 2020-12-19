from django.contrib import admin
from api.models import *

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=['id','name','city','roll']