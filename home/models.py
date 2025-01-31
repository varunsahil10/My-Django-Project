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
    # city = models.CharField(max_length=100)
    # age = models.IntegerField(null=True, blank=True)
    # gender = models.CharField(max_length=1, choices= GENDER_CHOICES)
    # email = models.EmailField()
    # dob = models.DateField(auto_now=False, auto_now_add=False)
    # image = models.ImageField(upload_to='student_image/', null=True, blank=True)


    def __str__(self):
        return str(self.roll) + ' - ' + self.name


#  One-to-One Relationship
class Address(models.Model):
    # city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.state
    

#  One-to-Many Relationship
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

#  Many-to-Many Relationship
class Course(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
    

#ORM

class Restaurant(models.Model):
    class Type(models.TextChoices):
        VEG = 'Veg'
        NON_VEG = 'Non-Veg'
        BOTH = 'Both'

    name = models.CharField(max_length=100)
    restaurant_type = models.CharField(max_length=10, choices=Type.choices)

class Rating(models.Model):
    rating = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='ratings')