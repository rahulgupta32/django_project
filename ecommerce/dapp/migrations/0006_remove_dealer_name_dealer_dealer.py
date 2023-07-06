# Generated by Django 4.2.2 on 2023-07-03 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0002_remove_company_name_company_company'),
        ('dapp', '0005_remove_dealer_dealer_dealer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='name',
        ),
        migrations.AddField(
            model_name='dealer',
            name='dealer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='capp.company'),
        ),
    ]
