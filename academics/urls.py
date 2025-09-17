from django.urls import path
from . import views

urlpatterns = [
    # ------------------ Classes ------------------ #
    path("classes/", views.manage_classes, name="manage_classes"),
    path("classes/add/", views.add_class, name="add_class"),
    path("classes/edit/<int:class_id>/", views.edit_class, name="edit_class"),
    path("classes/delete/<int:class_id>/", views.delete_class, name="delete_class"),

    # ------------------ Subjects ------------------ #
    path("subjects/", views.manage_subjects, name="manage_subjects"),
    path("subjects/add/", views.add_subject, name="add_subject"),
    path("subjects/edit/<int:subject_id>/", views.edit_subject, name="edit_subject"),
    path("subjects/delete/<int:subject_id>/", views.delete_subject, name="delete_subject"),

    # ------------------ Timetables ------------------ #
    path("timetables/", views.manage_timetables, name="manage_timetables"),
    path("timetables/add/", views.add_timetable, name="add_timetable"),
    path("timetables/edit/<int:timetable_id>/", views.edit_timetable, name="edit_timetable"),
    path("timetables/delete/<int:timetable_id>/", views.delete_timetable, name="delete_timetable"),
]
