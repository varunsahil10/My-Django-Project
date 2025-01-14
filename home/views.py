from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(form.cleaned_data)
            # data = form.cleaned_data
            # name = data['name']
            # roll = data['roll']

            # student = Student(name=name, roll=roll)
            form.save()

            return redirect('home')

    names = ['John', 'Doe', 'Jane']
    context = {
        'form': form,
        'names': names,
        'data' : '<b>dynamically generated html</b>',
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def dynamic_route(request,number):
    result = f"Table of {number} is :"
    for i in range(1,11):
       result += f"\n {number} * {i} = {number * i}"
    print(result) 
    return HttpResponse(result)

def search_student(request):
    students = Student.objects.all()

    print(request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        
        # searching name
        students = students.filter(name__icontains=search)

    if 'roll' in request.GET:
        roll = request.GET['roll']
        
        # searching roll
        if roll == '1':
            students = students.filter(roll__gte=1, roll__lte=50)
        
        elif roll == '2':
            students = students.filter(roll__gte=51)

    context = {
        'students': students
    }

    return render(request, 'search_student.html', context)

def search_teacher(request):
    teachers = Teacher.objects.all()

    print(request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        
        # searching name
        teachers = teachers.filter(
            Q(student__name__icontains=search) |
            Q(name__icontains=search) |
            Q(subject__icontains=search)
            
            )

    context = {
        'teachers': teachers,
    }

    return render(request, 'search_teacher.html', context)

