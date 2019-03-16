from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """docstring for HelloApiView."""

    def get(self, request, format=None):

        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'It is similar to a traditional Django view',
        'Give you control to your logic'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
