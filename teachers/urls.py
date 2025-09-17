from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_teachers, name='manage_teachers'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('assign-subject/<int:teacher_id>/', views.assign_subject, name='assign_subject'),
    # path('manage-subjects/', views.manage_teacher_subjects, name='manage_teacher_subjects'),
]
