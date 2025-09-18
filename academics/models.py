from django.db import models

# Create your models here.
class Subject(models.Model):
    class Meta:
        permissions = [
            ("manage_subject", "Can manage subject"),
        ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class StudentClass(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='main_classes')
    
    def __str__(self):
        return f"{self.class_name} - {self.section}"




class Timetable(models.Model):
    class Meta:
        pass
    DAYS_OF_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )

    student_class = models.ForeignKey('StudentClass', on_delete=models.CASCADE, related_name='timetables')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    
    def __str__(self):
        return f"{self.student_class} - {self.subject} - {self.day} {self.start_time}"
