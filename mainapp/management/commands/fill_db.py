from django.core.management.base import BaseCommand, CommandError
from mainapp.models import CategoryCourse, Course, Lesson, Schedule

class Command(BaseCommand):
    help = "Заполнение БД тестовыми данными"

    def handle(self, *args, **options):
        try:
            print('Очистка БД')
            Schedule.objects.all().delete()
            Lesson.objects.all().delete()
            Course.objects.all().delete()
            CategoryCourse.objects.all().delete()

            print('Заполнение БД')
            category = CategoryCourse.objects.create(name='Тестовые курсы')
            course = Course.objects.create(name='Таблица умножения', category = category)
            lesson1 = Lesson.objects.create(name='Таблица умножения на 2', course = course)
            lesson2 = Lesson.objects.create(name='Таблица умножения на 3', course = course)
            lesson3 = Lesson.objects.create(name='Зачет по таблице умножения на 2 и на 3', course = course)

            Schedule.objects.create(date='2023-09-02 08:45:00+07', lesson=lesson1)
            Schedule.objects.create(date='2023-09-05 09:00:00+07', lesson=lesson2)
            Schedule.objects.create(date='2023-09-09 08:00:00+07', lesson=lesson3)

            #teacher = User.objects.create()

            self.stdout.write(
                self.style.SUCCESS('Выполнено')
            )
        except BaseException as e:
            self.stdout.write(
                self.style.ERROR(e)
            )
        


