from celery import shared_task


@shared_task
def salary_total():
    from .models import Person
    persons = Person.objects.all()
    for person in persons:
        person.salary_total = int(person.salary_total)+int(person.salary_per_period)
        person.save()
