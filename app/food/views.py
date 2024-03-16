from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from food.models import Food
from food.serializers import FoodSerializer

dct = {
    "a": 1,
    "b": 2,
    "c": 3,
}


class WomenAPIView(APIView):
    def get(self, request):
        return Response(dct)


class FoodAPIView(ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
