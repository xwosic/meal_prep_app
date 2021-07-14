# Generated by Django 3.1.7 on 2021-06-13 14:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal_prep_app', '0026_recipe_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('amounts', models.ManyToManyField(to='meal_prep_app.Amount')),
                ('recipe_lists', models.ManyToManyField(to='meal_prep_app.RecipeList')),
                ('recipes', models.ManyToManyField(to='meal_prep_app.Recipe')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
