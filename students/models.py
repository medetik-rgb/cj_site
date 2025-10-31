from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    curator = models.CharField(max_length=100, verbose_name="Куратор")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название клуба")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.IntegerField(verbose_name="Возраст")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    clubs = models.ManyToManyField(Club, blank=True, verbose_name="Клубы")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
