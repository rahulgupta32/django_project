# Generated by Django 4.2.2 on 2023-07-09 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dapp', '0031_alter_dealer_dealer'),
        ('fsapp', '0012_alter_fieldstaff_company_alter_fieldstaff_dealer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldstaff',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldstaffs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fieldstaff',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fieldstaffs', to='dapp.dealer'),
        ),
    ]
