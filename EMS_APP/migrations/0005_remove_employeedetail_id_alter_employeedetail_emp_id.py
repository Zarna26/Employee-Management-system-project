# Generated by Django 5.0.1 on 2024-03-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS_APP', '0004_alter_employeedetail_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='emp_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
