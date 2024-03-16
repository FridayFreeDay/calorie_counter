from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from food.models import Food
from food.serializers import FoodSerializer


class FoodApiTestCase(APITestCase):
    def setUp(self):
        Food.objects.create(name='торт', calorie=123.00, weight=100.00)
        Food.objects.create(name='стейк', calorie=300.00, weight=250.00)

    def test_get(self):
        url = reverse('food-list')
        response = self.client.get(url)
        food = Food.objects.all()
        serializer_data = FoodSerializer(food, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(serializer_data[0]['name'], 'торт')
