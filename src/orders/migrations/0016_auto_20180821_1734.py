# Generated by Django 2.0.5 on 2018-08-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20180819_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'Paid'), (1, 'Waiting For Payment'), (0, 'In Progress')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.IntegerField(choices=[(0, 'Cash'), (1, 'Card')], default=1),
        ),
    ]
