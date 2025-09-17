from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["user", "date_of_birth", "gender", "student_class", "contact", "profile_image"]
        widgets = {
            "user": forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "date_of_birth": forms.DateInput(attrs={'type': 'date',
                # "placeholder": "Enter your date of birth",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "contact": forms.TextInput(attrs={
                "placeholder": "Enter your contact",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "gender": forms.Select(attrs={
                "placeholder": "Enter your gender",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "student_class": forms.Select(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
            "profile_image": forms.FileInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700"}),
        }
