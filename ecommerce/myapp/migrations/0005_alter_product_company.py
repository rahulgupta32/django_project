# Generated by Django 4.2.2 on 2023-07-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0003_alter_company_company'),
        ('myapp', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='capp.company'),
        ),
    ]
