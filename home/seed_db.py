from .models import *
from faker import Faker
from random import randint

fake = Faker('en_IN')

def generate_students(num = 10):
    for _ in range(num):
        student = Student(
            name=fake.name(), 
            roll=randint(1, 100),
        )
        student.save()


def generate_teachers(num = 10):
    for _ in range(num):
        teacher = Teacher(
            name=fake.name(),
            subject=fake.word(),
        )
        teacher.student = Student.objects.all()[randint(0, Student.objects.count()-1)]
        teacher.save()

# def generate_courses(num = 10):
#     for _ in range(num):
#         course = Course(
#             name=fake.word(),
#         )
#         course.student = Student.objects.all()[randint(0, Student.objects.count()-1)]
#         course.save()
