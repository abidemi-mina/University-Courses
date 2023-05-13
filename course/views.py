import re
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    faculies = Faculty.objects.all()
    about = About.objects.first()
    team = Team.objects.all()
    return render (request,'index.html' ,{'fact':faculies,'about':about,'team':team})

def team(request):
    team = Team.objects.all()
    return render (request,'team.html',{'team':team})

def course(request):
    courses = Department.objects.all()
    courses_cnt = Department.objects.all().count()
    fact = Faculty.objects.all()
    return render (request,'course.html',{'course':courses,'fact':fact,'count':courses_cnt,})

def faculty(request,slug):
    fac = Faculty.objects.get(slug=slug)
    fact = Faculty.objects.all()
    courses = Department.objects.filter(fac=fac).all()
    return render (request,'faculty.html',{'fact':fact,'fac':fac,'course':courses})

def course_detail(request,slug):
    course_det = Department.objects.get(slug=slug)
    job = Jobs.objects.filter(dept=course_det)
    return render (request,'course-detail.html',{'course_det':course_det,'job':job})