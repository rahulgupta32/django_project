# Generated by Django 4.2.3 on 2023-07-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
