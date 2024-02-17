from django.core.management.base import BaseCommand, CommandError
from mainapp.models import CategoryCourse, Course, Lesson, Schedule, MyEdu
from userapp.models import ScUser
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Заполнение БД тестовыми данными"

    def handle(self, *args, **options):
        try:
            print('Очистка БД')
            Schedule.objects.all().delete()
            Lesson.objects.all().delete()
            Course.objects.all().delete()
            CategoryCourse.objects.all().delete()
            MyEdu.objects.all().delete()
            # ScUser.objects.all().delete()

            print('создание учителя')
            teacher1 = ScUser.objects.create_user(username='teacher1', email='teacher@example.com', password='1', phone='123')
            teacher1.last_name = 'Учитель'
            teacher1.first_name = 'Семен'
            teacher1.save()
            group, _ = Group.objects.get_or_create(name='Teachers')
            group.user_set.add(teacher1)  # добавление пользователя в группу Teachers

            print('создание пользователя Создатель курсов')
            creator1 = ScUser.objects.create_user(username='creator1', email='creator1@example.com', password='1', phone='456')
            creator1.last_name = 'Создатель'
            creator1.first_name = 'Аркадий'
            creator1.save()
            group, _ = Group.objects.get_or_create(name='CourseCreators')
            group.user_set.add(creator1)  # добавление пользователя в группу Создатель курсов

            print('создание студента')
            student1 = ScUser.objects.create_user(username='student1', email='stud@example.com', password='1', phone='123')
            student1.last_name = 'Студент'
            student1.first_name = 'Саин'
            student1.save()

            print('Заполнение БД')
            category = CategoryCourse.objects.create(name='Открытые курсы', description='Курсы для свободного изучения всеми желающими')
            course1 = Course.objects.create(name='Таблица умножения', description='Курс предназначен для изучения таблицы умножения в начальных классах', category = category)
            lesson1 = Lesson.objects.create(name='Таблица умножения на 2', course=course1)
            lesson2 = Lesson.objects.create(name='Таблица умножения на 3', course=course1)
            lesson3 = Lesson.objects.create(name='Зачет по таблице умножения на 2 и на 3', course=course1)

            Schedule.objects.create(date='2023-09-02 08:45:00+07', lesson=lesson1)
            Schedule.objects.create(date='2023-09-05 09:00:00+07', lesson=lesson2)
            Schedule.objects.create(date='2023-09-09 08:00:00+07', lesson=lesson3)

            course2 = Course.objects.create(name='Все о треугольниках', description='Курс предназначен для изучения треугольников', category = category)
            lesson1 = Lesson.objects.create(name='Что такое треугольник?', course=course2)
            lesson2 = Lesson.objects.create(name='Остроугольный треугольник', course=course2)
            lesson3 = Lesson.objects.create(name='Прямоугольный треугольник', course=course2)
            lesson4 = Lesson.objects.create(name='Тупоугольный треугольник', course=course2)

            Schedule.objects.create(date='2023-09-02 08:00:00+07', lesson=lesson1)
            Schedule.objects.create(date='2023-09-05 09:30:00+07', lesson=lesson2)
            Schedule.objects.create(date='2023-09-09 12:00:00+07', lesson=lesson3)
            Schedule.objects.create(date='2023-09-09 08:00:00+07', lesson=lesson4)

            category = CategoryCourse.objects.create(name='Подготовка к ЕГЭ', description='Курсы для подготовки к ЕГЭ')

            for i in range(10):
                course3 = Course.objects.create(name='Подготовка к ЕГЭ по информатике №'+str(i), description='Курс предназначен для подготовке к ЕГЭ по информатике', category = category)
                lesson1 = Lesson.objects.create(name='Разбор задания №1', course=course3)
                lesson2 = Lesson.objects.create(name='Разбор задания №2', course=course3)
                lesson3 = Lesson.objects.create(name='Разбор задания №3', course=course3)

                course3.teachers.add(teacher1)
                course3.save()

                MyEdu.objects.create(course=course3, student=student1)

            Schedule.objects.create(date='2023-09-02 08:45:00+07', lesson=lesson1)
            Schedule.objects.create(date='2023-09-05 09:00:00+07', lesson=lesson2)
            Schedule.objects.create(date='2023-09-09 08:00:00+07', lesson=lesson3)

            print('Добавление преподавателей в курсы')
            course1.teachers.add(teacher1)
            course1.save()

            course2.teachers.add(teacher1)
            course2.teachers.add(creator1)
            course2.save()

            print('добавление курсов для студентов')
            # student1 course1

            self.stdout.write(
                self.style.SUCCESS('Выполнено')
            )
        except BaseException as e:
            self.stdout.write(
                self.style.ERROR(e)
            )
