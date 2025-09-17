from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'student_class', 'date', 'status')
    list_filter = ('status', 'student_class', 'date')
    search_fields = ('student__user__username', 'student__user__first_name', 'student__user__last_name')