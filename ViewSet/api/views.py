from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        serializer = StudentSerializer(Student.objects.get(id=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        student_object = Student.objects.get(id=pk)
        serializer = StudentSerializer(student_object, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student_object = Student.objects.get(id=pk)
        serializer = StudentSerializer(
            student_object, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Student.objects.get(id=pk).delete()
        return Response({'msg': 'deleted Successfully'}, status=status.HTTP_200_OK)
