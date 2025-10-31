from django.urls import path
from . import views

urlpatterns = [
    # Главная страница со списком студентов
    path('', views.student_list, name='student_list'),

    # Добавление нового студента
    path('add/', views.add_student, name='add_student'),

    # Приветственная страница (опционально)
    path('hello/', views.hello, name='hello'),

    # Регистрация пользователя
    path('register/', views.register, name='register'),
]
