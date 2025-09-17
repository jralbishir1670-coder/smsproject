from django.contrib import admin
from .models import Teacher, TeacherSubject

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact', 'email', 'profile_image')
    search_fields = ('username', 'user__first_name', 'user__last_name', 'email')
    # No filter_horizontal because subjects use 'through' table

@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject')
    search_fields = ('user__username', 'subject__name')
