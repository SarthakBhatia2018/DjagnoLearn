from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class LCStudentAPIView(ListAPIView,CreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


class LCStudentAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class RUDStudentAPIView(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


class RUDStudentAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
