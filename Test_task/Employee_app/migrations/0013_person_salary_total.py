# Generated by Django 3.2 on 2022-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_app', '0012_rename_salary_per_month_person_salary_per_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='salary_total',
            field=models.DecimalField(decimal_places=0, max_digits=7, null=True, verbose_name='Информация о выплаченной зарплате'),
        ),
    ]