from django.shortcuts import render, get_object_or_404, redirect 
from .models import Teacher, TeacherSubject
from django.contrib import messages
from .forms import TeacherForm, TeacherSubjectForm


# Create your views here.
# def manage_teachers(request):
#     teachers = Teacher.objects.all()
def manage_teachers(request):
    teachers = Teacher.objects.prefetch_related("subjects_assigned__subject").all()
    return render(request, "teachers/manage_teachers.html", {"teachers": teachers})

# def manage_teachers(request):
#     teachers = Teacher.objects.prefetch_related("subjects_assigned__subject").all()
#     return render(request, "teachers/manage_teachers.html", {"teachers": teachers})


def add_teacher(request):
    if  request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher added successfully.")
            return redirect("manage_teachers")
    else:
        form = TeacherForm()
    return render(request, "teachers/add_teacher.html", {"form": form})


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully.")
            return redirect("manage_teachers")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/edit_teacher.html", {"form": form, "teacher": teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':   
        teacher.delete()
        messages.success(request, "Teacher deleted successfully.")
        return redirect("manage_teachers")
    return render(request, 'teachers/delete_teacher.html', {"teacher": teacher}) 


# def manage_teacher_subjects(request):
#     teacher_subjects = TeacherSubject.objects.all()
#     return render(request, "teachers/manage_teacher_subjects.html", {"teacher_subjects": teacher_subjects})

def assign_subject(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id) 
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        if form.is_valid():
            teacher_subject = form.save(commit=False)
            teacher_subject.teacher = teacher   # ✅ attach teacher automatically
            teacher_subject.save()
            messages.success(request, "Subject assigned to teacher successfully.")
            return redirect("manage_teachers")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = TeacherSubjectForm()

    return render(request, "teachers/assign_subject.html", {"form": form, "teacher": teacher})


# def assign_subject(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id) 
#     if request.method == 'POST':
#         form = TeacherSubjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Subject assigned to teacher successfully.")
#             return redirect("manage_teachers")
#         else:
#             messages.error(request, "Please correct the error below.")
#     else:
#         form = TeacherSubjectForm()
#     return render(request, "teachers/assign_subject.html", {"form": form, "teacher": teacher})

