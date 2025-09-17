from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("teacher-dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student-timetable/", views.student_timetable, name="student_timetable"),
]
