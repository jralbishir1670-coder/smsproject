from django import forms
from .models import Teacher, TeacherSubject

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'contact', 'email', 'profile_image']
        widgets = {
            "user": forms.Select(attrs={
                # "placeholder": "Enter your full name",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "contact": forms.TextInput(attrs={
                "placeholder": "Enter your contact",
                "type": "text",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email",
                "type": "email",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "profile_image": forms.FileInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
        }


class TeacherSubjectForm(forms.ModelForm):
    class Meta:
        model = TeacherSubject
        fields = ["subject"]
        widgets = {
            # "teacher": forms.Select(attrs={
            #     "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "subject": forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
        }