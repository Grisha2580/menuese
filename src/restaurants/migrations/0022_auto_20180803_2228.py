# Generated by Django 2.0.5 on 2018-08-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0021_auto_20180803_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='restaurants_images/default.png', upload_to='restaurants_images'),
        ),
    ]
