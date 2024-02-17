from django.core.management.base import BaseCommand, CommandError
from mainapp.models import CategoryCourse, Course, Lesson, Schedule
from userapp.models import ScUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


class Command(BaseCommand):
    help = "Создание групп, назначение прав групп, создание суперадмина"

    def handle(self, *args, **options):
        try:
            print('Очистка БД: Удаление пользователей, групп, прав на группы')
            Group.objects.all().delete()
            ScUser.objects.all().delete()

            print('создание админа')
            admin = ScUser.objects.create_superuser(username='admin', email='admin@myproject.com', password='admin', phone='11111')
            admin.last_name = 'Администратор'
            admin.save()

            print('создание группы "Создатели курсов" (CourseCreators)')
            CourseCreator_group, _ = Group.objects.get_or_create(name='CourseCreators')
            perm = Permission.objects.filter(Q(codename='add_categorycourse') | Q(codename='change_categorycourse') | Q(codename='delete_categorycourse') | \
                Q(codename='add_course') | Q(codename='change_course') | Q(codename='delete_course') | \
                Q(codename='add_lesson') | Q(codename='change_lesson') | Q(codename='delete_lesson')) 
            CourseCreator_group.permissions.set(perm)

            print('создание группы "Учителя" (Teachers)')
            teacher_group, _ = Group.objects.get_or_create(name='Teachers')
            perm = Permission.objects.filter(Q(codename='change_course') | \
                Q(codename='add_lesson') | Q(codename='change_lesson') | Q(codename='delete_lesson') | \
                Q(codename='add_schedule') | Q(codename='change_schedule') | Q(codename='delete_schedule')) 
            teacher_group.permissions.set(perm)
            
            print('создание группы менеджер')
            manager_group, _ = Group.objects.get_or_create(name='Managers')
            perm = Permission.objects.filter(Q(codename='change_course') | \
                Q(codename='add_schedule') | Q(codename='change_schedule') | Q(codename='delete_schedule')) 
            manager_group.permissions.set(perm)

            # print('создание группы Студенты')
            # student_group, _ = Group.objects.get_or_create(name ='Students')
            # perm = Permission.objects.filter(Q(codename='view_categorycourse') | Q(codename='view_course'))
            # student_group.permissions.set(perm)

            self.stdout.write(
                self.style.SUCCESS('Выполнено')
            )
        except BaseException as e:
            self.stdout.write(
                self.style.ERROR(e)
            )
        


