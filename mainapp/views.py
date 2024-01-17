from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.conf import settings
from .models import CategoryCourse, Course, Lesson, Schedule
from .forms import CategoryCourseForm, CourseForm, ContactsForm

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
    model = CategoryCourse
    ordering = ['pk']
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(course_count = Count('course'))
        return queryset

    # template_name = ''
    # context_object_name =

    # get - гет запрос
    # get_context_data - передача контектса в шаблон
    # get_queryset - получение данных

class CategoryCourseCreateView(LoginRequiredMixin, CreateView):
    model = CategoryCourse
    form_class = CategoryCourseForm
    success_url = reverse_lazy('mainapp:categorycourse_list')

class CategoryCourseUpdateView(LoginRequiredMixin, UpdateView):
    model = CategoryCourse
    form_class = CategoryCourseForm
    success_url = reverse_lazy('mainapp:categorycourse_list')

class CategoryCourseDeleteView(LoginRequiredMixin, DeleteView):
    model = CategoryCourse
    success_url = reverse_lazy('mainapp:categorycourse_list')

class LessonListView(ListView):
    model = Lesson
    ordering = ['pk']

class CourseListView(ListView):
    model = Course
    ordering = ['pk']
    def get(self, request, *args, **kwargs):
        self.categorycourse_id = request.GET.get('categorycourse', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.categorycourse_id is not None:
            queryset = queryset.filter(category__id=self.categorycourse_id)

        queryset = queryset.select_related('category') # для оптимизации загрузки имени категории
        queryset = queryset.prefetch_related('teachers') # для оптимизации загрузки списка преподавателей
        return queryset
    

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('mainapp:course_list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('mainapp:course_list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('mainapp:course_list')

class CourseDetailView(DetailView):
    model = Course
