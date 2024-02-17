import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from mainapp.models import CategoryCourse, Course, Lesson, MyEdu  # , Schedule
from userapp.models import ScUser


class CategoryType(DjangoObjectType):
    class Meta:
        model = CategoryCourse
        fields = ("id", "name", "description")


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = '__all__'  # ("id", "name", "description", "category", "teachers")


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson
        fields = ("id", "name")


class ScUserType(DjangoObjectType):
    class Meta:
        model = ScUser
        fields = '__all__'
        exclude_fields = ['password']  # Прячем поле с паролем


class MyEduType(DjangoObjectType):
    class Meta:
        model = MyEdu
        fields = '__all__'


class Query(graphene.ObjectType):
    category_list = graphene.List(
        CategoryType,
        find=graphene.String(required=False),
        limit=graphene.Int(required=False),
        offset=graphene.Int(required=False))  # CategoryCourse.objects.all()
    course_list = graphene.List(
        CourseType,
        find=graphene.String(required=False),
        limit=graphene.Int(required=False),
        offset=graphene.Int(required=False))
    user_list = graphene.List(
        ScUserType,
        find=graphene.String(required=False),
        limit=graphene.Int(required=False),
        offset=graphene.Int(required=False))
    myedu_list = graphene.List(
        MyEduType,
        find=graphene.String(required=False),
        limit=graphene.Int(required=False),
        offset=graphene.Int(required=False))

    def resolve_category_list(self, info, find=None, limit=None, offset=None):
        queryset = CategoryCourse.objects.all()
        if find:
            queryset = queryset.filter(Q(name__icontains=find) | Q(description__icontains=find))

        if limit and offset:
            queryset = queryset[offset:offset+limit]

        return queryset

    def resolve_course_list(self, info, find=None, limit=None, offset=None):
        queryset = Course.objects.all()
        queryset = queryset.prefetch_related('teachers')
        if find:
            queryset = queryset.filter(Q(name__icontains=find) | Q(description__icontains=find))

        if limit and offset:
            queryset = queryset[offset:offset+limit]

        return queryset

    def resolve_user_list(self, info, limit=None, offset=None):
        queryset = ScUser.objects.all()

        if limit and offset:
            queryset = queryset[offset:offset+limit]

        return queryset

    def resolve_myedu_list(self, info, find=None, limit=None, offset=None):
        queryset = MyEdu.objects.all()
        queryset = queryset.select_related('course')
        queryset = queryset.select_related('student')
        if find:
            queryset = queryset.filter(Q(name__icontains=find) | Q(description__icontains=find))

        if limit and offset:
            queryset = queryset[offset:offset+limit]

        return queryset


schema = graphene.Schema(query=Query)
