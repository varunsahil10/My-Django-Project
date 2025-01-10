from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='student_image/', null=True, blank=True)


    def __str__(self):
        return self.name