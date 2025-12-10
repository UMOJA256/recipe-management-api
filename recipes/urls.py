from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, FavoriteRecipeViewSet, MealPlanViewSet, ShoppingListViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'favorites', FavoriteRecipeViewSet, basename='favorite')
router.register(r'mealplans', MealPlanViewSet, basename='mealplan')
router.register(r'shoppinglists', ShoppingListViewSet, basename='shoppinglist')

urlpatterns = [
    path('', include(router.urls)),
]

