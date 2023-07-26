# Generated by Django 4.2.3 on 2023-07-25 09:22

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0003_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_id', models.EmailField(max_length=100, unique=True)),
                ('phone_no', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, unique=True)),
                ('is_Company', models.BooleanField(default=False, verbose_name='Is Company')),
                ('is_Dealer', models.BooleanField(default=False, verbose_name='Is Dealer')),
                ('is_FieldStaff', models.BooleanField(default=False, verbose_name='Is FieldStaff')),
                ('is_Retailer', models.BooleanField(default=False, verbose_name='Is Retailer')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_custom', related_query_name='custom_user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_custom', related_query_name='custom_user', to='auth.permission')),
            ],
            options={
                'default_related_name': 'custom_users',
            },
        ),
    ]
