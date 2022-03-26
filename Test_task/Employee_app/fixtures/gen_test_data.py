from random import randrange, choice
import json

data = [{"model": "Employee_app.positions", "pk": 1, "fields": {"positions": "president"}},
        {"model": "Employee_app.positions", "pk": 2, "fields": {"positions": "base employee"}},
        {"model": "Employee_app.positions", "pk": 3, "fields": {"positions": "junior manager"}},
        {"model": "Employee_app.positions", "pk": 4, "fields": {"positions": "middle manager"}},
        {"model": "Employee_app.positions", "pk": 5, "fields": {"positions": "senior manager"}},
        {"model": "Employee_app.person", "pk": 1, "fields": {"last_name": "Boss", "first_name": "Boss", "middle_name": "Boss", "department": 4, "employment_date": "2021-03-22", "salary_per_period": "5000", "salary_total": "0", "person_rating": "0", "manager": None}},
        ]

positions = {1: 'base employee',
             2: 'junior manager',
             3: 'middle manager',
             4: 'senior manager'
             }

last_name = ['Test', 'Task']
first_name = ['Jon', 'Jane']
middle_name = ['Black', 'Write']
for i in range(2,100):
    gen_data = {}
    fields={}
    gen_data["model"] = "Employee_app.person"
    gen_data["pk"] = i
    fields["last_name"] = f"{choice(last_name)}{i}"
    fields["first_name"] = f"{choice(first_name)}{i}"
    fields["middle_name"] = f"{choice(middle_name)}{i}"
    fields["department"] = randrange(1, 5)
    fields["employment_date"] = "2021-03-22"
    fields["salary_per_period"] = f"{randrange(10, 50)}"
    fields["salary_total"] = f"{randrange(0, 500000)}"
    fields["person_rating"] = str(fields["department"])
    fields["manager"] = i-1
    gen_data["fields"] = fields
    data.append(gen_data)

with open('test_data.json', 'w') as outfile:
    json.dump(data, outfile)









