from rest_framework.serializers import ModelSerializer, Serializer
from mainapp.models import CategoryCourse, Course
from userapp.models import ScUser

class CategoryCourseModelSerializer(ModelSerializer):
    # преобразует данные model <--> json
    class Meta:
        model = CategoryCourse
        fields = '__all__'

class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ScUserModelSerializer(ModelSerializer):
    class Meta:
        model = ScUser
        fields = '__all__'