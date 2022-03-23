from django.db import models


class Positions(models.Model):
    positions = models.CharField(max_length=30, verbose_name='Должность')

    def __str__(self):
        return self.positions

    class Meta:

        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Person(models.Model):
    STANDARD = '4'
    J_MANAGER = '3'
    M_MANAGER = '2'
    S_MANAGER = '1'
    PRESIDENT = '0'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base'),
        (J_MANAGER, 'junior'),
        (M_MANAGER, 'middle'),
        (S_MANAGER, 'senior'),
        (PRESIDENT, 'president')
    )
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    department = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name='Должность')
    employment_date = models.DateField(verbose_name='Дата приема на работу')
    salary_per_period = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Заработная плата')
    salary_total = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='Информация о выплаченной зарплате',
                                       default=0)
    person_rating = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, verbose_name='Иерархия')
    manager = models.ForeignKey('self', models.SET_NULL, related_name='person', blank=True, null=True,
                                verbose_name='Менеджер')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
