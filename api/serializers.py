# from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer  # , Serializer
from mainapp.models import CategoryCourse, Course, MyEdu
from userapp.models import ScUser
from rest_framework import serializers


class CategoryCourseModelSerializer(serializers.ModelSerializer):
    # преобразует данные model <--> json
    # id = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='api:')
    # url = serializers.HyperlinkedIdentityField(view_name="mainapp:category-list")

    class Meta:
        model = CategoryCourse
        fields = '__all__'


class CourseModelSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='api:category-detail'
    )
    teachers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:user-detail'
    )

    class Meta:
        model = Course
        fields = '__all__'


class ScUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        # fields = '__all__'
        exclude = ['password']  # Прячем поле с паролем


class MyEduModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyEdu
        fields = '__all__'
