from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'It is similar to a traditional Django view',
        'Give you control to your logic'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})


    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):

        return Response({'method': 'put'})


    def patch(self, request, pk=None):

        return Response({'method': 'patch'})

    def delete(self,request, pk=None):

        return Response({'method': 'delete'})
