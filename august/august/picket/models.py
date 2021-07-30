from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255)
    joined_at = models.DateTimeField(auto_now_add=True)
    number_of_lessons = models.PositiveSmallIntegerField(default=0)

class Kelas(models.Model):
    name = models.CharField(max_length=255)
class Class_Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
