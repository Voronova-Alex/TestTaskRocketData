# Generated by Django 3.2 on 2022-03-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_app', '0011_rename_salary_per_period_person_salary_per_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='salary_per_month',
            new_name='salary_per_period',
        ),
    ]
