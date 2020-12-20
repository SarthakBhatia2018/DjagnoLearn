from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


class StudentAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id:
            try:
                student_obj = Student.objects.get(id=id)
            except:
                return Response({'msg': 'Does Not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer = StudentSerializer(student_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        student_object = Student.objects.get(id=id)
        if id:
            serializer = StudentSerializer(
                student_object, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            Student.objects.get(id=id).delete()
            return Response({'msg': 'Sucessfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'msg': 'Not Found'}, status=status.HTTP_400_BAD_REQUEST)
