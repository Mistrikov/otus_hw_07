from django.urls import path, include
from . import views

app_name = 'userapp'

urlpatterns = [
    
    #path('contacts/', views.contacts_view, name='contacts'),
    #path('categorycourse/update/<int:pk>/', views.CategoryCourseUpdateView.as_view(), name='categorycourse_update'),
    #path('course/list/', views.CourseListView.as_view(), name='course_list'),
    #path('course/list/<int:pk>', views.CourseListView.as_view(), name='course_list'),
    #path('register/', views.UserRegisterView.as_view(), name='register'),
    path('', views.index_view, name='index'),
]
