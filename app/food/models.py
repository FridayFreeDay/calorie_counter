from django.core.validators import MinValueValidator
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    calorie = models.DecimalField(max_digits=7,
                                  decimal_places=2,
                                  verbose_name='Калорийность/100г')
    weight = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 verbose_name="Вес/г",
                                 validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Питание'
        verbose_name_plural = 'Питание'

    def __str__(self):
        return f'{self.name}: {self.calorie * self.weight / 1000:.2f} ккал'
    