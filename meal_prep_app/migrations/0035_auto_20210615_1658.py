# Generated by Django 3.1.7 on 2021-06-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0034_remove_shoppinglist_amounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
