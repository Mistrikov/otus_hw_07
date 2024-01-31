from rest_framework.permissions import DjangoModelPermissions
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count
from django.conf import settings
from .models import CategoryCourse, Course, Lesson, Schedule
from .forms import CategoryCourseForm, CourseForm, ContactsForm
from django.core.paginator import Paginator

from .jobs import send_email_user
from .tasks import send_email_admin
import django_rq
from celery import Celery

def index_view(request):
    return render(request, 'mainapp/index.html')

def contacts_view(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            django_rq.enqueue(send_email_user, data=form.data)
            #django_rq.enqueue(send_email_admin, data=form.data)
            # отправляем письмо админам через celery
            send_email_admin.delay(data=form.data)
            return render(request, 'mainapp/contacts.html', {'messagesend': True})
    else:
        form = ContactsForm()

    return render(request, 'mainapp/contacts.html', {'form': form, 'messagesend': False})

class CategoryCourseListView(ListView):
    paginate_by = 6
    model = CategoryCourse
    ordering = ['pk']

    def get(self, request, *args, **kwargs):
        self.categorycourse_find = request.GET.get('categorycourse', None)
        return super().get(request, *args, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.categorycourse_find:
            queryset = queryset.filter(name__icontains=self.categorycourse_find)
        queryset = queryset.annotate(course_count = Count('course'))
        return queryset

    # template_name = ''
    # context_object_name =

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # get_queryset - получение данных

class CategoryCourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'mainapp.add_categorycourse'
    model = CategoryCourse
    form_class = CategoryCourseForm
    success_url = reverse_lazy('mainapp:categorycourse_list')

class CategoryCourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'mainapp.change_categorycourse'
    model = CategoryCourse
    form_class = CategoryCourseForm
    success_url = reverse_lazy('mainapp:categorycourse_list')

class CategoryCourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'mainapp.delete_categorycourse'
    model = CategoryCourse
    success_url = reverse_lazy('mainapp:categorycourse_list')

class CategoryCourseDetailView(DetailView):
    model = CategoryCourse
    

class LessonListView(ListView):
    model = Lesson
    ordering = ['pk']

class CourseListView(ListView):
    #permission_required = 'mainapp.view_course'
    paginate_by = 3
    model = Course
    ordering = ['pk']
    def get(self, request, *args, **kwargs):
        self.categorycourse_id = request.GET.get('categorycourse', None)
        self.course_find = request.GET.get('course', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.categorycourse_id:
            queryset = queryset.filter(category__id=self.categorycourse_id)
        
        if self.course_find:
            queryset = queryset.filter(name__icontains=self.course_find)

        queryset = queryset.select_related('category') # для оптимизации загрузки имени категории
        queryset = queryset.prefetch_related('teachers') # для оптимизации загрузки списка преподавателей
        return queryset
    

class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'mainapp.add_course'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('mainapp:course_list')

class CourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'mainapp.change_course'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('mainapp:course_list')

class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'mainapp.delete_course'
    model = Course
    success_url = reverse_lazy('mainapp:course_list')

class CourseDetailView(DetailView):
    model = Course
