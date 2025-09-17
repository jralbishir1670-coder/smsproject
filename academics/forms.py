from django import forms 
from .models import StudentClass, Subject, Timetable 

class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ['class_name', 'section', 'teacher']
        widgets = {
            "class_name" : forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "placeholder": "Enter class name",
            }),
            "section" : forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "placeholder": "Enter section",
            }),
            "teacher" : forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
        }
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code']
        widgets = {
            "name" : forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "placeholder": "Enter subject name",
            }),
            "code" : forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "placeholder": "Enter subject code",
               
            }),
            "teacher": forms.Select(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            }),
        }
        
        
class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['student_class', 'subject', 'teacher', 'day', 'start_time', 'end_time']
        widgets = {
            "student_class" : forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                
                
            }),
            "subject" : forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
            "teacher" : forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
            "day" : forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"
            }),
            "start_time" : forms.TimeInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "type": "time"
            }),
            "end_time" : forms.TimeInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring=2 focus:ring-blue-500 focus:border-blue-500 text-gray-700",
                "type": "time"
            }),
        }