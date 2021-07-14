from django.shortcuts import render
from .models import *


class Choice:
    """
    to use with choice_template.html
    create list of choices and inject it to form
    <button type="submit" name="{{choice.name}}" value="{{choice.value}}">{{choice.text}}</button>
    """
    def __init__(self, name="choice", value=0, text="choice 0"):
        self.name = name
        self.value = value
        self.text = text


# func adds to recipe a list of ingredients
def combine_details_about_recipe(recipe):
    recipe.list_of_amounts = Amount.objects.filter(recipe=recipe)
    for a in recipe.list_of_amounts:
        if a.amount.is_integer():
            a.amount = int(a.amount)
    return recipe


def get_user_recipe_lists(req):
    user = req.user
    return RecipeList.objects.filter(user=user)


def get_recipes_from_recipe_list(recipe_list):
    return recipe_list.recipes.all()


def show_req_post(req):
    for k, v in req.POST.items():
        print(f"{k}: {v}")


def choose_recipe(req):
    """
    renders under the same url choice view
    after clicking one of recipes this function isn't called again
    req.POST dictionary goes to view where the choose_recipe was called
    to catch recipe's primary key chosen by user use the code below in your view
    if req.method == 'POST':
        if 'chosen_recipe_pk' in req.POST:
            return get_object_or_404(Recipe, pk=req.POST['chosen_recipe_pk'])
    """
    show_req_post(req)
    recipes = Recipe.objects.all()

    choices = []
    for recipe in recipes:
        choices.append(Choice("chosen_recipe_pk", recipe.pk, recipe.title))

    res = {
        'question': "Wybierz przepis:",
        'choices': choices,
        'target_url': "",
    }
    return render(req, template_name='meal_prep_app/choice_template.html', context=res)


def ask_yes_or_no_question(req, question):
    """
    in view use this function like this:
    ...
    return ask_yes_or_no_question(req, question="Do you like ice cream?")

    in view you are using this function use code below to catch answer:
    if req.method == 'POST':
        if question in req.POST:
            answer = req.POST[question]
            if answer == 'Yes':
                do_sth()
            elif answer == 'No':
                do_sth_else()
    """
    res = {
        'question': question,
        'target_url': "",
    }
    return render(req, template_name='meal_prep_app/question_template.html', context=res)


def show_info(req, info):
    """
    takes list of string informations
    renders info under the same url, after clicking "Ok" goes back to normal view's work
    """
    return render(req, template_name='meal_prep_app/info_template.html', context={'info': info})


def get_amounts_from_recipes(recipes):
    amounts = []
    for recipe in recipes:
        amounts += list(Amount.objects.filter(recipe=recipe.pk))

    print(amounts)
    return amounts


def create_items_from_amounts(amounts, shopping_list):
    items = []
    for amount in amounts:
        item = Item()
        item.shopping_list = shopping_list,
        item.checked = False,
        item.ingredient = amount.ingredient,
        item.amount = amount.amount,
        item.unit = amount.unit
        items.append(item)

    return items

