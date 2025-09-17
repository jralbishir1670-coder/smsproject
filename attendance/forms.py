from django import forms 
from .models import Attendance 

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'student_class', 'date', 'status']
        widgets = {
            "student": forms.Select(attrs={
                 "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
            "student_class": forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
            'date': forms.DateInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "type": "date"
            }),
            'status': forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
        }