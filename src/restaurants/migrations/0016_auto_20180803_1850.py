# Generated by Django 2.0.5 on 2018-08-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0015_auto_20180803_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='/static/default.png', upload_to='restaurants_images'),
        ),
    ]
