import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 80),
        department=faker_ru.job(),
        salary=random.randint(1000, 10000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )

def generated_file():
    path = rf"D:\Program\PyCharm_program\Automation_UI\test{random.randint(0, 999)}.txt"
    file = open(path, 'w+')
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path

def generated_subject():
    subject = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
               "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]

    return subject[random.randint(0, len(subject)-1)]


def generated_state():
    state = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]

    return state[random.randint(0, len(state)-1)]

def accordian_choice():
    lst = ['first', 'second', 'third']
    return lst[random.randint(0, 2)]

def generator_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

def generate_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00',
    )
