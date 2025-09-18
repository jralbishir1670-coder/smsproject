from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from academics.models import Subject, Timetable
from attendance.models import Attendance


class Command(BaseCommand):
    help = "Set default group and permissions"
    
    def handle(self, *args, **kwargs):
        # Teacher Group
        teachers, _ = Group.objects.get_or_create(name="Teachers")
        subject_ct = ContentType.objects.get_for_model(Subject)
        attendance_ct = ContentType.objects.get_for_model(Attendance)
        timetable_ct = ContentType.objects.get_for_model(Timetable)
        
        manage_attendance = Permission.objects.get(
            codename="manage_attendance", content_type=attendance_ct
        )
        manage_subject = Permission.objects.get(
            codename="manage_subject", content_type=subject_ct
        )
        teachers.permissions.add(manage_attendance, manage_subject)
        
        # Student Group
        students, _ = Group.objects.get_or_create(name="Students")
        view_timetable = Permission.objects.get(
            codename="view_timetable", content_type=timetable_ct  # ✅ use built-in
        )
        students.permissions.add(view_timetable)
        
        self.stdout.write(self.style.SUCCESS("Roles and permissions created!"))
