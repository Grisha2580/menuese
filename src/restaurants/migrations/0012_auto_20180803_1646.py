# Generated by Django 2.0.5 on 2018-08-03 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20180730_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='type',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Type'),
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='DishType',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
