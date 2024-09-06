from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

@api_view()
def view_req(request):
    return Response( {'success':409, 'message':'api'})

# Create your views here.
@api_view(['PATCH','PUT','GET','POST'])
def view_Student(request):
    if request.method == 'GET':
        studentObj = Student.objects.all()
        serializer = StudentSerializer(studentObj,many=True)
        return Response({'msg':' get success','data':serializer.data},status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Student added success','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        studentObj = Student.objects.get(pk=request.data.get('id'))
        serializer = StudentSerializer(studentObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': ' Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        studentObj = Student.objects.get(pk=request.data.get('id'))
        serializer = StudentSerializer(studentObj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': ' Student updated successfully', 'data': serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg': 'Invalid request'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

