# Generated by Django 4.2.2 on 2023-06-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('capp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email_id', models.EmailField(max_length=254)),
                ('ph_no', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('experience_years', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capp.company')),
            ],
        ),
    ]
