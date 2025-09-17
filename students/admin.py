from django.contrib import admin
from .models import Student 

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'email', 'gender', 'student_class', 'contact', 'profile_image')
    list_filter = ('gender', 'student_class')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'contact')
