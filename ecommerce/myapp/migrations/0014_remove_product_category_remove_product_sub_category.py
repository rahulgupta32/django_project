# Generated by Django 4.2.2 on 2023-07-07 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_product_description_alter_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
    ]
