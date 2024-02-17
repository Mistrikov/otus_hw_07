from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ProfileUserForm, LoginUserForm, UserRegisterForm, UserPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.conf import settings


def index_view(request):
    return render(request, 'userapp/index.html')


class LogoutUser(LogoutView):
    success_url = reverse_lazy('mainapp:categorycourse_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'userapp/login.html'
    success_url = reverse_lazy('mainapp:categorycourse_list')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('userapp:profile')
    template_name = 'userapp/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user is not None:
            login(request=self.request, user=user)
        return response


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'userapp/profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('userapp:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeForm(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserPasswordChangeForm
    template_name = 'userapp/profile.html'
