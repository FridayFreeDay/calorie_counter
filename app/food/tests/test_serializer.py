from django.test import TestCase

from food.models import Food
from food.serializers import FoodSerializer


class FoodSerializerTestCase(TestCase):
    def test_ok(self):
        food1 = Food.objects.create(name='торт',
                                         calorie=123.00, weight=100.00)
        food2 = Food.objects.create(name='стейк',
                                         calorie=300.00, weight=250.00)

        food = Food.objects.all()
        serializer_data = FoodSerializer(food, many=True).data
        expected_data = [
            {
                'id': food1.id,
                'name': 'торт',
                'calorie': '123.00',
                'weight': '100.00',
            },
            {
                'id': food2.id,
                'name': 'стейк',
                'calorie': '300.00',
                'weight': '250.00',
            },
        ]
        self.assertEqual(expected_data, serializer_data)
