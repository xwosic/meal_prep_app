# Generated by Django 3.1.7 on 2021-03-18 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0008_auto_20210318_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ingredient_pk', to='meal_prep_app.ingredient'),
        ),
        migrations.AlterField(
            model_name='amount',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_pk', to='meal_prep_app.recipe'),
        ),
    ]
