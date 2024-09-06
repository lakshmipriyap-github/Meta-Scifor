from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializer import BookSerializer
from django.shortcuts import render

# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#

@api_view()
def view_req(request):
    return Response( {'success':409, 'message':'api'})

@api_view(['GET','POST','PUT','DELETE'])
def view_book(request):
    if request.method == 'GET':
        bookobj = Book.objects.all()
        serializer = BookSerializer(bookobj,many=True)
        return Response({'msg':' get success','data':serializer.data},status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' book added success','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        bookobj = Book.objects.get(pk=request.data.get('id'))
        serializer = BookSerializer(bookobj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' book updated success','data':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bookobj = Book.objects.get(pk=request.data.get('id'))
        bookobj.delete()
        return Response({'msg': ' book deleted success'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'msg':'Invalid request'},status=status.HTTP_405_METHOD_NOT_ALLOWED)