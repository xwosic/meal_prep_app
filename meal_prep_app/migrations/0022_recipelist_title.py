# Generated by Django 3.1.7 on 2021-03-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0021_recipelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipelist',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
