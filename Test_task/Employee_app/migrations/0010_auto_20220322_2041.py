# Generated by Django 3.2 on 2022-03-22 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_app', '0009_alter_person_employment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='salary_per_month',
            new_name='salary_per_period',
        ),
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.positions', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_rating',
            field=models.CharField(choices=[('4', 'base'), ('3', 'junior'), ('2', 'middle'), ('1', 'senior'), ('0', 'president')], max_length=25, verbose_name='Иерархия'),
        ),
    ]
