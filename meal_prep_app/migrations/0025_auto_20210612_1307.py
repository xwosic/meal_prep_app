# Generated by Django 3.1.7 on 2021-06-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0024_auto_20210612_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
