from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from recipes.views import RecipeViewSet, FavoriteRecipeViewSet, MealPlanViewSet, ShoppingListViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'favorites', FavoriteRecipeViewSet, basename='favorite')
router.register(r'mealplans', MealPlanViewSet, basename='mealplan')
router.register(r'shoppinglists', ShoppingListViewSet, basename='shoppinglist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # All our ViewSets are under /api/
    
    # JWT Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
