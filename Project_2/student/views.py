from django.shortcuts import render
from .models import Student
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    students = Student.objects.all()
    return render (request, 'student/index.html',{"student" : students})


def create_form(request):
    return render (request, 'student/create_form.html')


def create_data(request):
    # return render (request, 'student/create_data.html')
    # return HttpResponse("Ok")
    the_name = request.POST.get('name')
    the_title = request.POST.get('title')
    new_student = Student(name=the_name, title=the_title)
    new_student.save()
    return HttpResponseRedirect(reverse('index'))