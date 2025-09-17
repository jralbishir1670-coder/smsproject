from django.contrib import admin
from .models import StudentClass, Subject, Timetable

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'teacher')
    search_fields = ('class_name', 'section', 'teacher__user__username')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    # search_fields = ('subject_name',)
    search_fields = ("name", "", "teacher__full_name")
    # list_filter = ("teacher",)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('student_class', 'subject', 'teacher', 'day', 'start_time', 'end_time')
    list_filter = ('day', 'student_class')
    search_fields = ('student_class__name', 'subject__name', 'teacher__user__username')