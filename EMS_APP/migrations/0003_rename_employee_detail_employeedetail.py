# Generated by Django 5.0.1 on 2024-03-02 11:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMS_APP', '0002_rename_employeedetail_employee_detail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee_Detail',
            new_name='EmployeeDetail',
        ),
    ]
