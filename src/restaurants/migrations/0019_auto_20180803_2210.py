# Generated by Django 2.0.5 on 2018-08-03 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0018_auto_20180803_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='/Users/Apple/Projects/menuese/src/static', upload_to='restaurants_images/%'),
        ),
    ]
