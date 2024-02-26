from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('contacts/', views.contacts_view, name='contacts'),
    # path('testlogin/', views.testlogin_view, name='testlogin'),
    path('categorycourse/list/', views.CategoryCourseListView.as_view(), name='categorycourse_list'),
    path('categorycourse/create/', views.CategoryCourseCreateView.as_view(), name='categorycourse_create'),
    path('categorycourse/update/<int:pk>/', views.CategoryCourseUpdateView.as_view(), name='categorycourse_update'),
    path('categorycourse/delete/<int:pk>/', views.CategoryCourseDeleteView.as_view(), name='categorycourse_delete'),
    path('categorycourse/<int:pk>/', views.CategoryCourseDetailView.as_view(), name='categorycourse_detail'),
    path('course/list/', views.CourseListView.as_view(), name='course_list'),
    path('course/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('lesson/list/', views.LessonListView.as_view(), name='lesson_list'),
    path('myedu/list/', views.MyEduListView.as_view(), name='myedu_list'),
    path('myedu/delete/<int:pk>/', views.MyEduDeleteView.as_view(), name='myedu_delete'),
    path('', views.index_view, name='index'),
]
