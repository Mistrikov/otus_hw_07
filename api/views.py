from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets, mixins
# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from mainapp.models import CategoryCourse, Course
from userapp.models import ScUser
from .serializers import CategoryCourseModelSerializer, CourseModelSerializer, ScUserModelSerializer
# from .filters import CategoryCourseFilter
# from .permissions import OnlyForTeachers
from django.db.models import Q


# пагинация
class ScLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class CategoryCourseViewSet(viewsets.ModelViewSet):
    queryset = CategoryCourse.objects.all()
    serializer_class = CategoryCourseModelSerializer
    pagination_class = ScLimitOffsetPagination
    # permission_classes = [DjangoModelPermissions] # права автоматически назначаются на модели, выкл для тестов
    # permission_classes = [IsAuthenticated]
    # permission_classes = [OnlyForTeachers] # описан в permissions.py

    def get_queryset(self):
        category_find = self.request.query_params.get('find', '')
        queryset = CategoryCourse.objects.all()
        if category_find:
            queryset = queryset.filter(Q(name__icontains=category_find) | Q(description__icontains=category_find))
        return queryset


# для сложных фильтров используется отдельный файл, например, filters.py
# тогда поиск может быть по нескольким полям
'''class CategoryCourseViewSet(viewsets.ModelViewSet):
    queryset = CategoryCourse.objects.all()
    serializer_class = CategoryCourseModelSerializer
    filterset_class = CategoryCourseFilter'''

# ##### course ########

# 1 вариант просмотра списка курсов, одного курса и т.д.
# class CourseViewSet(viewsets.ModelViewSet):
#    serializer_class = CourseModelSerializer
#    queryset = Course.objects.all()

# 2 вариант просмотра списка курсов, одного курса и т.д.
# надо самому писать функции list, put, delete и т.д.
'''class CourseViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def course_text_only(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        return Response({'course.full_name': course.title_name}) # метод из модели как свойство класса

    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseModelSerializer(course)
        return Response(serializer.data)
'''

# 3 вариант через миксины (как бы кирпичики, можно комбинировать)
# типа самый удобный :)


class CourseViewSet(
        mixins.CreateModelMixin,  # добавление
        mixins.ListModelMixin,  # список
        mixins.RetrieveModelMixin,  # детали, 1 элемент
        mixins.DestroyModelMixin,  # удаление
        viewsets.GenericViewSet,  # должен быть последним
        ):

    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    pagination_class = ScLimitOffsetPagination
    permission_classes = [DjangoModelPermissions]  # права автоматически назначаются на модели

    def get_queryset(self):
        course_find = self.request.query_params.get('find', '')
        queryset = Course.objects.all()
        if course_find:
            queryset = queryset.filter(Q(name__icontains=course_find) | Q(description__icontains=course_find))
        return queryset


class ScUserViewSet(
        mixins.CreateModelMixin,  # добавление
        mixins.ListModelMixin,  # список
        mixins.RetrieveModelMixin,  # детали, 1 элемент
        mixins.DestroyModelMixin,  # удаление
        viewsets.GenericViewSet,  # должен быть последним
        ):

    queryset = ScUser.objects.all()
    serializer_class = ScUserModelSerializer
    pagination_class = ScLimitOffsetPagination
    permission_classes = [DjangoModelPermissions]  # права автоматически назначаются на модели

    def get_queryset(self):
        user_find = self.request.query_params.get('find', '')
        user_group = self.request.query_params.get('group', '')
        queryset = ScUser.objects.all()
        if user_find:
            queryset = queryset.filter(name__icontains=user_find)
        if user_group:
            queryset = queryset.filter(groups__in=user_group)
        return queryset
