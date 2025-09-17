from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages 


# Create your views here.
def home(request):
    return render(request, 'students/home.html')

def manage_students(request):
    students = Student.objects.all()
    return render(request, 'students/manage_students.html', {'students': students}) 

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('manage_students')
    else:
        # This handles GET requests
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('manage_students')
    return render(request, 'students/delete_student.html', {'student': student})