
from django.shortcuts import render
from django.http import JsonResponse
from .models import Commet
from .serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def comments(request):
    if request.method == 'GET':
        post2 = Commet.objects.all()
        serializer = CommentSerializer(post2, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET','PUT','DELETE'])
def detail(request,pk):
    try:
        commenta = Commet.objects.get(pk=pk)
    except Commet.DoesNotExist:
        return Response(
            status= status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = CommentSerializer(commenta)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = CommentSerializer(commenta, data=request.data)
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
        commenta.delete()
        return Response(
            'Delete successfully',
            status=status.HTTP_202_ACCEPTED

        )

