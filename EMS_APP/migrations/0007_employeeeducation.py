# Generated by Django 5.0.1 on 2024-03-09 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS_APP', '0006_remove_employeedetail_country'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_pg', models.CharField(max_length=200, null=True)),
                ('school_clg_pg', models.CharField(max_length=200, null=True)),
                ('percentage_pg', models.CharField(max_length=100, null=True)),
                ('course_grad', models.CharField(max_length=200, null=True)),
                ('school_clg_grad', models.CharField(max_length=200, null=True)),
                ('year_of_Passing_grad', models.DateField(max_length=100, null=True)),
                ('percentage_grad', models.DateField(max_length=100, null=True)),
                ('course_ssc', models.CharField(max_length=200, null=True)),
                ('school_clg_ssc', models.CharField(max_length=200, null=True)),
                ('year_of_Passing_ssc', models.CharField(max_length=100, null=True)),
                ('percentage_ssc', models.CharField(max_length=100, null=True)),
                ('course_hsc', models.CharField(max_length=200, null=True)),
                ('school_clg_hsc', models.CharField(max_length=200, null=True)),
                ('year_of_Passing_pg', models.CharField(max_length=100, null=True)),
                ('percentage_hsc', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
