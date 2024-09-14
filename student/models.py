from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    City = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Name


def student(request):
    return None