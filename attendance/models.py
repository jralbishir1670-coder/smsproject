from django.db import models

# Create your models here.
class Attendance(models.Model):
    class Meta:
        permissions = [
            ("manage_attendance", "Can manage attendance"),
        ]
    
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendances')
    student_class = models.ForeignKey('academics.StudentClass', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

   