from django.contrib import admin
from .models import Recipe, Amount, Ingredient, RecipeList, ShoppingList, Item


class AmountInline(admin.TabularInline):
    model = Amount
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [AmountInline]


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class ShoppingListAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


# class RecipeInline(admin.TabularInline):
#     model = Recipe
#     extra = 1
#
#
# class RecipeListAdmin(admin.ModelAdmin):
#     inlines = [RecipeInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeList)  #, RecipeListAdmin)
admin.site.register(Ingredient)
admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(Item)
admin.site.register(Amount)
