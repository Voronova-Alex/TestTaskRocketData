# Generated by Django 3.2 on 2022-03-22 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_app', '0010_auto_20220322_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='salary_per_period',
            new_name='salary_per_month',
        ),
    ]
