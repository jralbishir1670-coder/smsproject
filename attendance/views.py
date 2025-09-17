from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from students.models import Student
from django.contrib import messages
from academics.models import StudentClass
from .forms import AttendanceForm


# Manage Attendance
def manage_attendance(request):
    attendance_records = Attendance.objects.select_related("student", "student_class").order_by("-date")
    return render(request, "attendance/manage_attendance.html", {"attendance_records": attendance_records})


# Add Attendance
def add_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance recorded successfully.")
            return redirect("manage_attendance")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AttendanceForm()
    return render(request, "attendance/add_attendance.html", {"form": form})


# Edit Attendance
def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance updated successfully.")
            return redirect("manage_attendance")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, "attendance/edit_attendance.html", {"form": form, "attendance": attendance})


# Delete Attendance
def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == "POST":
        attendance.delete()
        messages.success(request, "Attendance deleted successfully.")
        return redirect("manage_attendance")
    return render(request, "attendance/delete_attendance.html", {"attendance": attendance})


# Attendance Report

