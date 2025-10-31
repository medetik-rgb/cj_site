from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views   # 👈 добавили

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),  # 👈 добавили
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),                                   # 👈 добавили

    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
