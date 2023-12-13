from django.db import models
from django.contrib.auth.models import User

class CategoryCourse(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    category = models.ForeignKey(CategoryCourse, on_delete=models.PROTECT)
    teachers = models.ManyToManyField(User)
    #students = models.ManyToManyField(User) 

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=64, unique=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    date = models.DateTimeField(auto_now=False, null=False) # , format="%d.%m.%Y %H:%M"
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    
    