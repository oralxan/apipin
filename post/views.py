
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .serializers import PosttSerialializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def postsss(request):
    if request.method == 'GET':
        post2 = Post.objects.all()
        serializer = PosttSerialializer(post2, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PosttSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET','PUT','DELETE'])
def detail(request,pk):
    try:
        posa = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = PosttSerialializer(posa)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = PosttSerialializer(posa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status= status.HTTP_202_ACCEPTED

            )
        return Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
    elif request.method == 'DELETE':
        posa.delete()
        return Response(
            'Delete successfully',
            status=status.HTTP_202_ACCEPTED

        )

