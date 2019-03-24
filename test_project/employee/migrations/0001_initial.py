# Generated by Django 2.1.7 on 2019-03-20 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('profession', models.CharField(max_length=100, default='-')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('EmployeeID', models.IntegerField(default=0)),
                ('First_Name', models.CharField(max_length=200, verbose_name='First Name', default='-')),
                ('Middle_Name', models.CharField(max_length=200, verbose_name='Middle Name', default='-')),
                ('Last_Name', models.CharField(max_length=200, verbose_name='Last Name', default='-')),
                ('Prefix', models.CharField(max_length=200, verbose_name='Prefix', default='-')),
                ('Nickname', models.CharField(max_length=200, verbose_name='Nickname', default='-')),
                ('Gender', models.CharField(choices=[('W', 'Woman'), ('M', 'Man')], default='W', max_length=1, verbose_name='Gender')),
                ('Birth_date', models.DateField(default=django.utils.timezone.now)),
                ('Passport_Surname', models.CharField(max_length=200, verbose_name='Passport Surname', default='-')),
                ('Passport_Given_Name', models.CharField(max_length=200, verbose_name='Passport Given Name', default='-')),
                ('Job_Title', models.CharField(max_length=200, verbose_name='Job Title', default='-')),
                ('Business_Phone', models.CharField(max_length=12, verbose_name='Business Phone', default='-')),
                ('Location', models.CharField(max_length=200, verbose_name='Location', default='-')),
                ('Hire_Date', models.DateField(default=django.utils.timezone.now)),
                ('Record_Status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default='0', verbose_name='Record Status')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
