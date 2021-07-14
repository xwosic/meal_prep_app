# Generated by Django 3.1.7 on 2021-06-14 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0028_auto_20210613_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_pk', to='meal_prep_app.recipe'),
        ),
    ]
