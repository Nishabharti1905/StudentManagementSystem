from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect

from student.models import Student, Student


# Create your views here.
def home(request):
    return render(request, 'home.html')


def display_studs(request):
    students = Student.objects.all()
    data = {'students': students}
    return render(request, 'displaystudent.html', data)





@login_required
def add_studs(request):
    if request.method == 'GET':
        return render(request, 'addstudent.html')

    else:
        student = Student()
        student.Name = request.POST['tbname']
        student.Age = request.POST['tbage']
        student.City = request.POST['tbcity']
        student.Email = request.POST['tbemail']
        student.Phone = request.POST['tbphone']
        student.save()
        return redirect('displaystudents')

@login_required
def edit_studs(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'GET':
        data = {"student": student}
        return render(request, "editstudent.html", data)

    else:
        student.Name = request.POST["tbname"]
        student.Age = request.POST["tbage"]
        student.City = request.POST["tbcity"]
        student.Email = request.POST["tbemail"]
        student.Phone = request.POST["tbphone"]
        student.save()
        return redirect('displaystudents')


@login_required
def delete_studs(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('displaystudents')


def login_fun(request):
    if request.method == "GET":
        return render(request, 'login.html')

    else:
        uname = request.POST['tbusername']
        pword = request.POST['tbpass1']
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            request.session['name'] = user.username
            return redirect('home')
        else:
            return redirect('login')


def register_fun(request):
    if request.method == "GET":
        return render(request, 'register.html')

    else:
        p1 = request.POST['tbpass1']
        p2 = request.POST['tbpass2']
        un = request.POST['tbusername']
        em = request.POST['tbemail']
        if p1 == p2:
            u = User.objects.create_superuser(un, em, p1)
            u.save()
            return redirect('login')
        else:
            return redirect('register')


def logout_fun(request):
    del request.session['name']
    logout(request)
    return redirect('login')