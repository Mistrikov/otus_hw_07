from rest_framework.serializers import ModelSerializer, Serializer
from mainapp.models import CategoryCourse

class CategoryCourseModelSerializer(ModelSerializer):
    # преобразует данные model <--> json
    class Meta:
        model = CategoryCourse
        fields = '__all__'

