from django.contrib import admin

from food.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
