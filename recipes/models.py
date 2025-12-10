from django.db import models
from django.contrib.auth.models import User

# Recipe Model
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
        ('Snack', 'Snack'),
        ('Beverage', 'Beverage'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="List ingredients separated by commas")
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    def __str__(self):
        return self.title

# Favorite Recipe Model
class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favorited_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"

# Meal Plan Model
class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mealplans")
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, related_name="mealplans")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

# Shopping List Model
class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shoppinglists")
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, related_name="shoppinglists")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
