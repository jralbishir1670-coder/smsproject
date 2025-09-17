from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from academics.models import Subject

class Command(BaseCommand):
    help = "Setup default groups and permissions"

    def handle(self, *args, **kwargs):
        # Teacher Group
        teachers, _ = Group.objects.get_or_create(name="Teachers")
        subject_ct = ContentType.objects.get_for_model(Subject)
        add_subject = Permission.objects.get(codename="add_subject", content_type=subject_ct)
        change_subject = Permission.objects.get(codename="change_subject", content_type=subject_ct)
        teachers.permissions.add(add_subject, change_subject)

        # Student Group
        students, _ = Group.objects.get_or_create(name="Students")
        view_subject = Permission.objects.get(codename="view_subject", content_type=subject_ct)
        students.permissions.add(view_subject)

        self.stdout.write(self.style.SUCCESS("Roles and permissions created!"))
