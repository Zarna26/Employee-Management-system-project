# Generated by Django 5.0.1 on 2024-03-02 11:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMS_APP', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeDetail',
            new_name='Employee_Detail',
        ),
    ]
