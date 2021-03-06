# Generated by Django 3.2 on 2022-03-22 06:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', models.CharField(max_length=30, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('employment_date', models.DateField(auto_now_add=True, verbose_name='Дата приема на работу')),
                ('salary_per_month', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Заработная плата')),
                ('salary_total', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Заработная плата')),
                ('person_rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Иерархия')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee_app.positions')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['-department', 'person_rating'],
            },
            managers=[
                ('all_employees', django.db.models.manager.Manager()),
            ],
        ),
    ]
