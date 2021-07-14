from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
# Create your models here.

UNITS = [
        ('', ''),
        ('g', 'g'),
        ('kg', 'kg'),
        ('l', 'l'),
        ('ml', 'ml'),
        ('szklanka', 'szklanka'),
        ('łyżka', 'łyżka'),
        ('łyżeczka', 'łyżeczka'),
        ('ząbek', 'ząbek'),
        ('szczypta', 'szczypta')
    ]


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, blank=False, unique=True, null=False)
    pub_date = models.DateField(blank=False)
    preparation_time = models.DurationField(default=timedelta(hours=1))
    people = models.PositiveSmallIntegerField(default=2)
    # img1 = models.ImageField()
    description = models.TextField()
    # img2 = models.ImageField()
    # img3 = models.ImageField()
    recipe = models.TextField(blank=False, default="Przykładowy przepis:"
                                                   "\n1. Przygotuj składniki"
                                                   "\n2. Wymieszaj"
                                                   "\n3. Gotowe!")

    def __str__(self):
        return f"{self.title}"


class Ingredient(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False, unique=True, help_text="Name of the ingredient")

    def __str__(self):
        return f"{self.name}"


class Amount(models.Model):
    # DO NOT CHANGE THE ORDER OF THE LIST!!!
    # new tuples add on the bottom of the list
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='amounts')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_pk', null=True)
    amount = models.FloatField(default=0.0, help_text='Amount of ingredient', blank=False)
    unit = models.CharField(max_length=15, choices=UNITS, blank=True, default='')
    short_description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.amount} {self.unit} {self.ingredient}"


class RecipeList(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False, default="")
    user = models.ManyToManyField(User)
    recipes = models.ManyToManyField(Recipe, related_name='recipe_lists')

    def __str__(self):
        return f"{self.title}"


class ShoppingList(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, default="")
    user = models.ManyToManyField(User, related_name='shopping_lists')
    # amounts = models.ManyToManyField(Amount, blank=True)
    # recipes = models.ManyToManyField(Recipe, blank=True)
    recipe_lists = models.ManyToManyField(RecipeList, blank=True, related_name='shopping_lists')
    # recipe_list = models.OneToOneField(RecipeList, on_delete=models.CASCADE, blank=False, primary_key=True,
    #                                    related_name='shopping_list', default=RecipeList.objects.get(pk=0))

    def __str__(self):
        return f"{self.title}"


class Item(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0.0, help_text='Amount of ingredient', blank=False)
    unit = models.CharField(max_length=15, choices=UNITS, blank=True, default='')

    def __str__(self):
        return f"{self.amount} {self.unit} {self.ingredient}"
