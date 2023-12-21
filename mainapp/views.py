from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CategoryCourse, Course, Lesson, Schedule
from .forms import CategoryCourseForm, UserRegisterForm, CourseForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView

def index_view(request):
    return render(request, 'mainapp/index.html')

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')

class CategoryCourseListView(ListView):
    model = CategoryCourse
    ordering = ['pk']
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
    #fields = '__all__'
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
        return queryset
    

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('mainapp:course_list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    #fields = '__all__'
    success_url = reverse_lazy('mainapp:course_list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('mainapp:course_list')

class CourseDetailView(DetailView):
    model = Course
    

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('mainapp:categorycourse_list')
    template_name = 'registration/register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context
