from django.contrib import admin
from .models import Student, Group, Club


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "curator")
    search_fields = ("name", "curator")
    ordering = ("name",)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "group", "display_clubs", "photo_preview")
    list_filter = ("group", "clubs")
    search_fields = ("first_name", "last_name")
    ordering = ("last_name",)
    
    def display_clubs(self, obj):
        """Отображение всех клубов студента в одной строке"""
        return ", ".join([club.name for club in obj.clubs.all()])
    display_clubs.short_description = "Клубы"

    def photo_preview(self, obj):
        """Отображение миниатюры фото (если есть)"""
        if obj.photo:
            return f"<img src='{obj.photo.url}' width='60' height='60' style='object-fit: cover; border-radius: 5px;' />"
        return "—"
    photo_preview.short_description = "Фото"
    photo_preview.allow_tags = True
