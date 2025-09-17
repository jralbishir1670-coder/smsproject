from django.urls import path
from . import views

urlpatterns = [
    # Attendance CRUD
    path("manage/", views.manage_attendance, name="manage_attendance"),
    path("add/", views.add_attendance, name="add_attendance"),
    path("edit/<int:attendance_id>/", views.edit_attendance, name="edit_attendance"),
    path("delete/<int:attendance_id>/", views.delete_attendance, name="delete_attendance"),

    # Attendance Report
    # path("report/", views.attendance_report, name="attendance_report"),
]
