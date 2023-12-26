from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Course2(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student2(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course2)

    def __str__(self):
            return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student2, on_delete=models.CASCADE)
    course = models.ForeignKey(Course2, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.login
