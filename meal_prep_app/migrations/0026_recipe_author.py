# Generated by Django 3.1.7 on 2021-06-13 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal_prep_app', '0025_auto_20210612_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]
