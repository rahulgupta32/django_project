# Generated by Django 4.2.3 on 2023-07-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0016_remove_company_email_id_remove_company_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email_id',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_no',
            field=models.CharField(blank=True, default='+977-', max_length=15, null=True),
        ),
    ]
