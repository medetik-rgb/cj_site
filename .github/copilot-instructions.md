## Быстрая справка для AI-агентов — проект "cj_site"

Ниже — короткие, практичные указания, чтобы быстро стать продуктивным в этом репозитории (Django, минимальный учебный сайт со студентами).

- Ядро: Это однопроцессный Django-проект. Точка входа — `manage.py` и настройки в `college_site/settings.py`.
- Приложение: основное приложение — `students` (модели в `students/models.py`, представления в `students/views.py`, маршруты в `students/urls.py`, шаблоны в `students/templates/students/`).
- База данных: SQLite файл `db.sqlite3` в корне; настройки БД находятся в `college_site/settings.py` (dev, DEBUG=True).
- Статические и медиа: статические файлы обслуживаются из `students/static/` через стандартный `STATIC_URL='/static/'`. Медиа-файлы сохраняются в `media/` (`MEDIA_ROOT = BASE_DIR / 'media'`). В `college_site/urls.py` при DEBUG=True добавлено `static()` для медиа.

Чего ожидать в коде (коротко):
- Модель `Student` содержит поля `first_name`, `last_name`, `age`, `group`, `photo`.
- Представления: `student_list` рендерит `students/index.html` и получает список студентов через `Student.objects.all()`. `add_student` обрабатывает POST-форму без Django Forms (простая ручная обработка `request.POST` и `request.FILES`). Есть также простое `hello`-представление.
- Маршруты: корень проекта направлен на `students.urls` (в корне — список студентов), маршруты в `students/urls.py`: `''` -> `student_list`, `hello/`, `add/`.

Процессы разработки и проверки (как запускать):
- Установи зависимости для Django (проект не содержит `requirements.txt`). Обычно:
  - python -m pip install django
- Запуск dev-сервера:
  - python manage.py runserver
- Миграции (если потребуется):
  - python manage.py makemigrations
  - python manage.py migrate

Проектные соглашения и паттерны, важные для изменений (конкретно в этом репо):
- Нет форм Django — формы обрабатываются вручную в `views.add_student`. При изменениях проверяй `enctype="multipart/form-data"` в шаблоне `students/add_student.html` и использование `request.FILES`.
- Шаблоны используют `{% load static %}` и относительные пути: CSS лежит в `students/static/students/style.css`.
- Тексты локализованы на русский; `college_site/settings.py` содержит `LANGUAGE_CODE = 'ru'` и `TIME_ZONE = 'Asia/Almaty'`.
- Файлы изображений хранятся в `media/photos/` (см. `upload_to='photos/'` в модели `Student`). При работе с тестовыми данными учитывай, что поле `photo` может быть пустым (`blank=True, null=True`).

Ключевые файлы для изменений и ревью (с примечанием, что там смотреть):
- `students/models.py` — модель `Student` (поля и upload_to)
- `students/views.py` — логика CRUD (простая, без форм и сериализаторов)
- `students/urls.py` — маршруты приложения
- `students/templates/students/index.html` и `add_student.html` — где находятся формы и вывод
- `college_site/settings.py` — DEBUG, MEDIA_ROOT, INSTALLED_APPS

Частые правки, которые можно встретить в PR:
- Добавление валидации формы: обычно добавляют Django Forms или ручную валидацию в `add_student`.
- Безопасность: проект в dev-режиме (DEBUG=True). При релизе нужно убрать секретные ключи из `settings.py` и настроить ALLOWED_HOSTS.
- Статические/медиа: для тестов убедись, что `MEDIA_ROOT` существует и сервер отдает `/media/` при DEBUG.

Примеры задач с подсказками (как автоматизировать изменения):
- Добавить поле email в `Student`:
  - Обновить `students/models.py` (CharField/EmailField), создать миграцию, обновить шаблоны (`index.html`, `add_student.html`) и `views.add_student` чтобы читать `request.POST.get('email')`.
- Заменить ручную обработку формы на Django Form:
  - Создать `students/forms.py` с `StudentForm`, использовать `form = StudentForm(request.POST, request.FILES)` в `add_student`.

Что не трогать без проверки:
- `college_site/settings.py` содержит SECRET_KEY в репозитории — не публикуй его наружу и не заменяй в PR без указания альтернативы. Для production используйте переменные окружения.

Где искать тесты: `students/tests.py` — сейчас пустой. Добавляйте модульные тесты в этот файл или в `students/tests/`.

Если нужно больше контекста или примеров кода, спроси, какие области приоритетнее: тесты, формы, API (DRF) или деплой.

---
Если инструкция зашла не в ту сторону, подскажи, какие сценарии AI-агент должен уметь выполнять: e.g., "исправить баг в форме", "добавить API для Student", "написать unit test" — и я дополню файл.
