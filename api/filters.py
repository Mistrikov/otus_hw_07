from django_filters import rest_framework as filters
from mainapp.models import CategoryCourse


class CategoryCourseFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CategoryCourse
        fields = ['name', 'description']
