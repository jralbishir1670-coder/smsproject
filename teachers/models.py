from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='teacher_profiles/', default='teacher_profiles/default.png')

    # subjects will be linked through TeacherSubject
    def __str__(self):
        return self.user.get_full_name()


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects_assigned")
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} - {self.subject}"