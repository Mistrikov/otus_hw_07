from django.db import models
from userapp.models import ScUser


class CategoryCourse(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    description = models.TextField(max_length=1024, unique=False, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    description = models.TextField(max_length=1024, unique=False, null=True)
    category = models.ForeignKey(CategoryCourse, on_delete=models.PROTECT)
    teachers = models.ManyToManyField(ScUser)

    def __str__(self):
        return self.name

    # свои методы в модели как свойство класса
    @property
    def title_name(self):
        return f'{self.name} ({self.category.name})'


class Lesson(models.Model):
    name = models.CharField(max_length=64, unique=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField(unique=False, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date = models.DateTimeField(auto_now=False, null=False)  # , format="%d.%m.%Y %H:%M"
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)


class ContactMessage(models.Model):
    name = models.TextField(null=False, default='Незнакомец')
    topic = models.TextField(max_length=128, null=False, default='Вопрос с сайта')
    message_text = models.TextField(max_length=512, null=False, default='Пусто')
    email = models.EmailField(null=False, unique=False)
    date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.message_text[:128]+'...'


class MyEdu(models.Model):
    student = models.ForeignKey(ScUser, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True, null=False)
    finish_date = models.DateTimeField(null=True)
