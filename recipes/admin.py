from django.contrib import admin
from .models import Recipe, FavoriteRecipe, MealPlan, ShoppingList

admin.site.register(Recipe)
admin.site.register(FavoriteRecipe)
admin.site.register(MealPlan)
admin.site.register(ShoppingList)
