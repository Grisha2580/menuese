# Generated by Django 2.0.5 on 2018-08-04 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180804_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
    ]