from rest_framework.viewsets import ModelViewSet, ViewSet
from mainapp.models import CategoryCourse
from .serializers import CategoryCourseModelSerializer

class CategoryCourseViewSet(ModelViewSet):
    queryset = CategoryCourse.objects.all()
    serializer_class = CategoryCourseModelSerializer