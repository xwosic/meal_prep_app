from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Ingredient, Amount, RecipeList, ShoppingList, Item
from .forms import RecipeForm, AmountForm, IngredientForm, RecipeListForm, ShoppingListForm, ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from .utils import *


def home(req):
    return render(req, 'meal_prep_app/home.html')


def all_recipes(req):
    show_req_post(req)
    recipes = Recipe.objects.all()

    res = {
        'recipes': recipes,
    }
    return render(req, 'meal_prep_app/all_recipes.html', context=res)


def detail(req, recipe_pk):
    show_req_post(req)
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    recipe = combine_details_about_recipe(recipe)
    if req.method == 'POST':
        if 'info' in req.POST:
            info = [f"Tytuł: {recipe.title}", f"Autor: {recipe.author.username}"]
            return show_info(req, info)
    context = {
        'recipe': recipe,
        'request_username': req.user.username,
    }
    return render(req, template_name='meal_prep_app/detail.html', context=context)


@login_required
def user_recipe_lists(req):
    return render(req, 'meal_prep_app/user_lists.html', context={'user_lists': get_user_recipe_lists(req)})


@login_required
def recipe_list(req, list_pk):
    show_req_post(req)
    list_of_recipes = get_object_or_404(RecipeList, pk=list_pk)
    if req.method == 'POST':
        if "recipe_to_remove" in req.POST:
            recipe_to_remove = get_object_or_404(Recipe, pk=req.POST["recipe_to_remove"])
            list_of_recipes.recipes.remove(recipe_to_remove)

        if 'chosen_recipe_pk' in req.POST:
            recipe = get_object_or_404(Recipe, pk=req.POST['chosen_recipe_pk'])
            list_of_recipes.recipes.add(recipe)

        if 'add_recipe' in req.POST:
            return choose_recipe(req)

        if 'create_shopping_list' in req.POST:
            # user clicked "shopping list"
            shopping_list = ShoppingList()
            shopping_list.title = f"Lista zakupów: {list_of_recipes.title}"
            shopping_list.save()
            shopping_list.user.add(req.user)
            shopping_list.recipe_lists.add(list_of_recipes)
            return redirect('meal_prep_app:create_shopping_list', shopping_list.pk)

    recipes = list_of_recipes.recipes.all()
    for recipe in recipes:
        choice = Choice("recipe_to_remove", recipe.pk, "Usuń z listy")
        recipe.choice = choice

    res = {
        "list_name": list_of_recipes.title,
        "list_of_recipes": recipes,
    }
    return render(req, template_name='meal_prep_app/list_of_recipes.html', context=res)


@login_required
def new_recipe(req):
    show_req_post(req)
    recipe_form = RecipeForm()

    if req.method == 'POST':
        # recipe_form.title.validate()
        recipe = recipe_form.save(commit=False)
        recipe.author = req.user
        recipe.title = req.POST['title']
        recipe.pub_date = datetime.date.today()
        recipe.preparation_time = datetime.timedelta(hours=1)
        recipe.recipe = "Przykładowy przepis:\n1. Przygotuj składniki\n2. Wymieszaj\n3. Gotowe!"
        recipe.people = 2
        recipe.description = ""
        recipe.save()
        return redirect('meal_prep_app:edit_recipe', recipe.pk)

    res = {
        'new_recipe_form': recipe_form,
    }
    return render(req, 'meal_prep_app/new_recipe.html', context=res)


@login_required
def edit_recipe(req, recipe_pk):
    show_req_post(req)

    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    if recipe.author != req.user:
        return show_info(req, ["To nie twój przepis!", "Nie możesz go edytować."])

    amounts = Amount.objects.filter(recipe=recipe)
    form = RecipeForm(req.POST or None, req.FILES or None, instance=recipe)
    amount_form = AmountForm()
    delete_question = f"Czy na pewno chesz usunąć ten przepis? {recipe.title}"
    if req.method == 'POST':
        if 'ingredient' in req.POST:
            # adding new amount of ingredient
            amount_form = AmountForm(req.POST)
            if amount_form.is_valid():
                amount = amount_form.save(commit=False)
                amount.recipe = recipe
                amount.save()
                # when submit in form, the data in other forms is not in req.POST dict
                form = RecipeForm(instance=recipe)
                amount_form = AmountForm()

        if 'title' in req.POST:
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.save()
                return redirect('meal_prep_app:recipes')

        if 'delete_recipe' in req.POST:
            # user clicked delete button
            return ask_yes_or_no_question(req, delete_question)

        if delete_question in req.POST:
            if req.POST[delete_question] == "Yes":
                # user confirmed deleting recipe
                recipe.delete()
                return redirect('meal_prep_app:recipes')

    is_recipe_new = not form.is_valid()
    print(is_recipe_new)

    res = {
        'edit_recipe_form': form,
        'amount_form': amount_form,
        'amounts': amounts,
        'is_recipe_new': is_recipe_new,
    }

    return render(req, 'meal_prep_app/edit_recipe.html', context=res)


@login_required
def user_recipes(req):
    recipes = Recipe.objects.filter(author=req.user.pk)
    res = {
        'recipes': recipes,
    }
    return render(req, template_name="meal_prep_app/user_recipes.html", context=res)


@login_required
def new_recipe_list(req):
    recipe_list_form = RecipeListForm(req.POST or None, req.FILES or None)
    if req.method == 'POST':
        if recipe_list_form.is_valid():
            recipe_list = recipe_list_form.save()
            recipe_list.user.add(req.user)
            return redirect('meal_prep_app:user_lists')
    res = {
        'recipe_list_form': recipe_list_form,
    }
    return render(req, template_name='meal_prep_app/new_recipe_list.html', context=res)


@login_required
def add_recipe_to_user_list(req, recipe_pk):
    show_req_post(req)
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    user_lists = get_user_recipe_lists(req)

    if req.method == 'POST':
        if 'chosen_recipe_list_pk' in req.POST:
            # user clicked one of his/her recipe list
            chosen_recipe_list = get_object_or_404(RecipeList, pk=req.POST['chosen_recipe_list_pk'])
            chosen_recipe_list.recipes.add(recipe)
            return redirect('meal_prep_app:recipe_list', req.POST['chosen_recipe_list_pk'])

        if 'Anuluj' in req.POST:
            return redirect('meal_prep_app:detail', recipe.pk)

    choices = []
    for u_list in user_lists:
        choice = Choice("chosen_recipe_list_pk", u_list.pk, u_list.title)
        choices.append(choice)

    question = f"Wybierz listę, do której dodać {recipe.title}"
    res = {
        'question': question,
        'choices': choices,
        'target_url': "",
    }
    return render(req, template_name='meal_prep_app/choice_template.html', context=res)


@login_required
def create_shopping_list(req, list_pk):
    show_req_post(req)
    shopping_list = ShoppingList.objects.prefetch_related('recipe_lists').get(pk=list_pk)
    recipe_lists = list(RecipeList.objects.filter(shopping_lists=list_pk))
    print(recipe_lists)
    recipes = [get_recipes_from_recipe_list(r_list) for r_list in shopping_list.recipe_lists.all()]
    print(recipes)
    # items += recipe_items
    item_form = ItemForm(req.POST or None)

    if req.method == 'POST':
        if 'add_item' in req.POST:
            item = item_form.save(commit=False)
            item.shopping_list = shopping_list
            item.save()
            item_form = ItemForm()

    items = list(Item.objects.filter(shopping_list=shopping_list))

    res = {
        # 'recipes': recipes,
        'items': items,
        'item_form': item_form,
    }
    return render(req, template_name='meal_prep_app/new_shopping_list.html', context=res)


# def edit_shopping_list(req, list_pk):
#     shopping_list = get_object_or_404(ShoppingList, pk=list_pk)
#     recipe_lists = shopping_list.recipe_lists.all()
#     recipes = shopping_list.recipes.all()
#     amounts = shopping_list.amounts.all()
#     # for recipe_list in recipe_lists:
#     #     recipes += recipe_list.recipes.all()
#     #
#     # for recipe in recipes:
#     #     amounts += Amount.objects.filter(recipe=recipe)
#     res = {
#         'recipe_lists': recipe_lists,
#         'recipes': recipes,
#         'amounts': amounts,
#     }
#     return render(req, template_name='meal_prep_app/edit_shopping_list.html', context=res)

