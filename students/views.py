from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Student, Group, Club
from .forms import RegisterForm


def hello(request):
    return HttpResponse("Добро пожаловать на сайт колледжа!")


@login_required
def student_list(request):
    """Страница со списком студентов, их групп и клубов"""
    students = Student.objects.select_related('group').prefetch_related('clubs').all()
    return render(request, 'students/index.html', {'students': students})


@login_required
def add_student(request):
    """Форма добавления нового студента"""
    groups = Group.objects.all()
    clubs = Club.objects.all()

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        group_id = request.POST.get("group")
        photo = request.FILES.get("photo")
        club_ids = request.POST.getlist("clubs")  # список выбранных клубов

        group = Group.objects.get(id=group_id)
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            group=group,
            photo=photo
        )

        # добавляем выбранные клубы
        if club_ids:
            student.clubs.set(club_ids)

        return redirect("student_list")

    return render(request, "students/add_student.html", {"groups": groups, "clubs": clubs})


def register(request):
    """Регистрация нового пользователя"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)  # авторизация сразу после регистрации
            return redirect("student_list")
        else:
            # если форма невалидна — отобразить ошибки
            return render(request, "students/register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "students/register.html", {"form": form})

