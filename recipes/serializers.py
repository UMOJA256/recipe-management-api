from rest_framework import serializers
from .models import Recipe, FavoriteRecipe, MealPlan, ShoppingList

# Recipe Serializer
class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'category', 'prep_time', 'cook_time', 'servings',
            'created_at', 'author'
        ]

# Favorite Recipe Serializer
class FavoriteRecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), source='recipe', write_only=True
    )

    class Meta:
        model = FavoriteRecipe
        fields = ['id', 'user', 'recipe', 'recipe_id', 'added_at']

# Meal Plan Serializer
class MealPlanSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipes = RecipeSerializer(many=True, read_only=True)
    recipe_ids = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), many=True, source='recipes', write_only=True
    )

    class Meta:
        model = MealPlan
        fields = ['id', 'user', 'name', 'recipes', 'recipe_ids', 'created_at']

# Shopping List Serializer
class ShoppingListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipes = RecipeSerializer(many=True, read_only=True)
    recipe_ids = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), many=True, source='recipes', write_only=True
    )

    class Meta:
        model = ShoppingList
        fields = ['id', 'user', 'name', 'recipes', 'recipe_ids', 'created_at']
