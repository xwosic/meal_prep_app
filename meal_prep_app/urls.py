from django.urls import path
from . import views

app_name = 'meal_prep_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes', views.all_recipes, name='recipes'),
    path('recipes/<int:recipe_pk>', views.detail, name='detail'),
    path('recipes/new_recipe', views.new_recipe, name='new_recipe'),
    path('recipes/edit_recipe/<int:recipe_pk>', views.edit_recipe, name='edit_recipe'),
    path('recipes/user_recipes/', views.user_recipes, name="user_recipes"),
    path('choose_recipe', views.choose_recipe, name="choose_recipe"),
    path('user_recipe_lists', views.user_recipe_lists, name='user_lists'),
    path('recipe_list/<int:list_pk>', views.recipe_list, name='recipe_list'),
    path('user_recipe_lists/new_recipe_list', views.new_recipe_list, name='new_recipe_list'),
    path('user_recipe_lists/add_recipe/<int:recipe_pk>', views.add_recipe_to_user_list, name='add_recipe_to_user_list'),
    path('create_shopping_list/<int:list_pk>', views.create_shopping_list, name='create_shopping_list'),
]

# path('edit_shopping_list/<int:list_pk>', views.edit_shopping_list, name="edit_shopping_list"),
