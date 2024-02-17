from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('registration/', views.UserRegisterView.as_view(), name='registration'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('changepassword/', views.UserPasswordChangeForm.as_view(), name='changepassword'),
    path('', views.index_view, name='index'),
]
