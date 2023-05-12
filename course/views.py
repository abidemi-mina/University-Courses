import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'index.html')

def team(request):
    return render (request,'team.html')

def course(request):
    return render (request,'course.html')

def faculty(request):
    return render (request,'faculty.html')

def course_det(request):
    return render (request,'course-detail.html')