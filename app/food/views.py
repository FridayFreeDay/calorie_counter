from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

dct = {
    "a": 1,
    "b": 2,
    "c": 3,
}


class WomenAPIView(APIView):
    def get(self, request):
        return Response(dct)