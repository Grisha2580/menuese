# Generated by Django 2.0.5 on 2018-07-19 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20180504_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='adress',
            new_name='address',
        ),
    ]
