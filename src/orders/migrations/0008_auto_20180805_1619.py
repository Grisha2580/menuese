# Generated by Django 2.0.5 on 2018-08-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180805_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Paid'), (2, 'Waiting For Payment'), (3, 'In Progress')], default=3),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Card')], default=2),
        ),
    ]
