from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import StudentClass, Subject, Timetable
from .forms import StudentClassForm, SubjectForm, TimetableForm
# from django.contrib.models   import reverse


# ---------------------- Student Classes ---------------------- #
# def manage_classes(request):
#     classes = StudentClass.objects.all().order_by("subject_name",)
#     return render(request, "academics/manage_classes.html", {"classes": classes})

def manage_classes(request):
    classes = StudentClass.objects.all().order_by("class_name", "section")
    return render(request, "academics/manage_classes.html", {"classes": classes})


def add_class(request):
    if request.method == "POST":
        form = StudentClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class added successfully.")
            return redirect("manage_classes")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentClassForm()
    return render(request, "academics/add_class.html", {"form": form})


def edit_class(request, class_id):
    student_class = get_object_or_404(StudentClass, id=class_id)
    if request.method == "POST":
        form = StudentClassForm(request.POST, instance=student_class)
        if form.is_valid():
            form.save()
            messages.success(request, "Class updated successfully.")
            return redirect("manage_classes")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentClassForm(instance=student_class)
    return render(request, "academics/edit_class.html", {"form": form, "student_class": student_class})


def delete_class(request, class_id):
    student_class = get_object_or_404(StudentClass, id=class_id)
    if request.method == 'POST':    
        student_class.delete()
        messages.success(request, "Class deleted successfully.")
        return redirect("manage_classes")
    return render(request, "academics/delete_class.html", {"student_class": student_class})


# ---------------------- Subjects ---------------------- #
def manage_subjects(request):
    subjects = Subject.objects.all().order_by("name")
    return render(request, "academics/manage_subjects.html", {"subjects": subjects})

# def manage_subjects(request):
#     subjects = Subject.objects.all().order_by("name")
#     return render(request, "academics/manage_subjects.html", {"subjects": subjects})


def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject added successfully.")
            return redirect("manage_subjects")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubjectForm()
    return render(request, "academics/add_subject.html", {"form": form})


def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully.")
            return redirect("manage_subjects")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubjectForm(instance=subject)
    return render(request, "academics/edit_subject.html", {"form": form, "subject": subject})


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, "Subject deleted successfully.")
        return redirect("manage_subjects")
    return render(request, "academics/delete_subject.html", {"subject": subject})

    # return render(request, "academics/delete_stuject.html", {"subject": subject})


# ---------------------- Timetable ---------------------- #
def manage_timetables(request):
    timetables = Timetable.objects.select_related("student_class", "subject", "teacher").order_by("student_class", "day", "start_time")
    return render(request, "academics/manage_timetables.html", {"timetables": timetables})


def add_timetable(request):
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Timetable entry added successfully.")
            return redirect("manage_timetables")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TimetableForm()
    return render(request, "academics/add_timetable.html", {"form": form})


def edit_timetable(request, timetable_id):
    timetable = get_object_or_404(Timetable, id=timetable_id)
    if request.method == "POST":
        form = TimetableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            messages.success(request, "Timetable updated successfully.")
            return redirect("manage_timetables")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TimetableForm(instance=timetable)
    return render(request, "academics/edit_timetable.html", {"form": form, "timetable": timetable})


def delete_timetable(request, timetable_id):
    timetable = get_object_or_404(Timetable, id=timetable_id)
    if request.method == 'POST':
        timetable.delete()
        messages.success(request, "Timetable entry deleted successfully.")
        return redirect("manage_timetables")
    return render(request, "academics/delete_timetable.html", {"timetable": timetable})
