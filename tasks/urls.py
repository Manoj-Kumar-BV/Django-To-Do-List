from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.mark_completed, name='mark_completed')  # Ensure this line is present
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
