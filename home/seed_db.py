from .models import *
from faker import Faker
from random import randint

fake = Faker('en_IN')

def generate_students():
    for _ in range(10):
        student = Student(
            name=fake.name(), 
            roll=randint(1, 100),
        )
        student.save()