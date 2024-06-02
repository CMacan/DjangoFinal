from django.db import models

def default_profile_pic():
    return "images/avatar.jpg"

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pics/', default=default_profile_pic, blank=True, null=True)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'