
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group 
# from .forms import RegisterForm
from .forms import RegisterForm
# from django.urls import reverse 
# from .models import User
from django.utils import timezone
from students.models import Student
from teachers.models import Teacher
from academics.models import StudentClass, Subject, Timetable
from attendance.models import Attendance



# Create your views here.
def index(request):
    return render(request, "home/index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Assign user to "Students" group by default
            students_group = Group.objects.get(name="Students")
            user.groups.add(students_group)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})
    return render(request, "accounts/login.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    user = request.user
    if not user.is_active:
        return render(request, "accounts/inactive.html") 
    if user.is_superuser:
        return redirect("admin_dashboard")
    if user.is_staff:
        return redirect("staff_dashboard")
    if user.groups.filter(name="Teachers").exists():
        return redirect("teacher_dashboard")
    if user.groups.filter(name="Students").exists():
        return redirect("student_dashboard")
    return render(request, "accounts/no_role.html")
    
 
@login_required
def admin_dashboard(request):
     # Stats
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    class_count = StudentClass.objects.count()
    subject_count = Subject.objects.count()
    attendance_count = Attendance.objects.count()

    # Example recent activities (you can replace with real logging system later)
    recent_activities = [
        {"icon": "user", "color": "text-blue-500", "message": "New student registered", "timestamp": timezone.now()},
        {"icon": "book", "color": "text-green-500", "message": "New class added", "timestamp": timezone.now()},
        {"icon": "check-circle", "color": "text-indigo-500", "message": "Attendance marked", "timestamp": timezone.now()},
    ]

    context = {
        "student_count": student_count,
        "teacher_count": teacher_count,
        "class_count": class_count,
        "subject_count": subject_count,
        "attendance_count": attendance_count,
        "recent_activities": recent_activities,
    }
    return render(request, "accounts/admin_dashboard.html", context)

@login_required
def staff_dashboard(request):
    return render(request, "accounts/staff_dashboard.html")

@login_required
def teacher_dashboard(request):
    return render(request, "accounts/teacher_dashboard.html")

@login_required
def student_dashboard(request):
    user = request.user
    student = getattr(user, 'student_profile', None)
    present_days = absent_days = attendance_percent = 0
    if student:
        present_days = student.attendances.filter(status='present').count()
        absent_days = student.attendances.filter(status='absent').count()
        total_days = present_days + absent_days
        attendance_percent = int((present_days / total_days) * 100) if total_days > 0 else 0
    # Placeholder for activities (no model found)
    activities = [
        "Member, Science Club",
        "Captain, Debate Team",
        "Volunteer, Environmental Awareness Program"
    ]
    context = {
        'student': student,
        'present_days': present_days,
        'absent_days': absent_days,
        'attendance_percent': attendance_percent,
        'activities': activities,
    }
    return render(request, "accounts/student_dashboard.html", context)

@login_required
def student_timetable(request):
    user = request.user
    student = getattr(user, 'student_profile', None)
    timetable = []
    if student and student.student_class:
        timetable = Timetable.objects.filter(student_class=student.student_class).select_related('subject', 'teacher').order_by('day', 'start_time')
    return render(request, 'accounts/student_timetable.html', {'timetable': timetable})


   
    
    
    
    
 