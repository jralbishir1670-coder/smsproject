from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_class = models.ForeignKey('academics.StudentClass', on_delete=models.SET_NULL, null=True, related_name='students')
    contact = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='student_profiles/', default='student_profiles/default.png')
    
    def __str__(self):
        return self.user.get_full_name()