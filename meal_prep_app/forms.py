from django.forms import ModelForm
from .models import Recipe, Amount, Ingredient, RecipeList, ShoppingList, Item


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'title', 'pub_date', 'preparation_time', 'people', 'description', 'recipe']


class AmountForm(ModelForm):
    class Meta:
        model = Amount
        fields = ['ingredient', 'amount', 'unit', 'short_description']
        # extra = 1


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['ingredient', 'amount', 'unit']


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeListForm(ModelForm):
    class Meta:
        model = RecipeList
        fields = ['title', 'recipes']


class ShoppingListForm(ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['title', 'recipe_lists']
