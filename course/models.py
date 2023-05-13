from django.db import models
from django.shortcuts import reverse
# from collectionfield.models import CollectionField


# Create your models here.
class About(models.Model):
    description = models.TextField(null=True,blank=True)

    def __str__(self) :
        return 'About Website'

    class Meta():
        verbose_name_plural = 'About'


class Team(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    dept = models.CharField(max_length=100,null=True,blank=True)
    img = models.ImageField(help_text='Upload your image ',null=True,blank=True)

    def team_img(self):
        if self.img:
            return self.img.url

    def __str__(self) :
        return self.name

    class Meta():
        verbose_name_plural = ' Team Members'

class Department(models.Model):
    AGRICULTURE = 'Agricultural Science'
    ARTS = 'Arts'
    BIOLOGY = 'Biological Science'
    MANAGEMENT = 'Management Science'
    DENSITRY = 'Densitry'
    EDUCATION = 'Education'
    ENGNIEERING = 'Engineering'
    HEANDTECH = 'Health Science and Technology'
    LAW = 'Law'
    MEDSCIENCE = 'Medical Science'
    PHARM = 'Pharmaceutical Science'
    PHYSCIENCE = 'Physical Science'
    VETMED = 'Veterinary Medicine'
    CHOOSE = ''
    FACULTIES = [
        ( AGRICULTURE,'Agricultural Science'),
        (  ARTS , 'Arts'),
        (  BIOLOGY, 'Biological Science'),
        (  MANAGEMENT ,'Management Science'),
        ( DENSITRY, 'Densitry'),
        ( EDUCATION ,'Education'),
        ( ENGNIEERING ,'Engineering'),
        ( HEANDTECH, 'Health Science and Technology'),
        ( LAW, 'Law'),
        ( MEDSCIENCE, 'Medical Science'),
        (  PHARM ,'Pharmaceutical Science'),
        ( PHYSCIENCE ,'Physical Science'),
        (  VETMED ,'Veterinary Medicine'),
        (CHOOSE, 'Choose A Faculty'),
    ]
    name = models.CharField(max_length=100, null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank=True)
    fac = models.CharField(max_length=100,choices=FACULTIES, default=CHOOSE,verbose_name='Faculty')
    f_slug = models.SlugField(max_length=200,null=True,blank=True,verbose_name='faculty slug')
    job = models.TextField(null=True,blank=True)
    desc = models.TextField(null=True,blank=True,verbose_name='Description')

    def __str__(self) :
        return self.name

    def jobs(self):
        if self.job:
            data = len(self.job)
            return data

    def get_dept_url(self):
        return reverse("course_det",args=[self.slug])

    class Meta():
        verbose_name_plural = 'Departments'

class Jobs(models.Model):
    name= models.CharField(max_length=20,null=True,blank=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Course')

    def __str__(self) :
        return self.name

    class Meta():
            verbose_name_plural = 'Jobs'

class Faculty(models.Model):
    AGRICULTURE = 'Agricultural Science'
    ARTS = 'Arts'
    BIOLOGY = 'Biological Science'
    MANAGEMENT = 'Management Science'
    DENSITRY = 'Densitry'
    EDUCATION = 'Education'
    ENGNIEERING = 'Engineering'
    HEANDTECH = 'Health Science and Technology'
    LAW = 'Law'
    MEDSCIENCE = 'Medical Science'
    PHARM = 'Pharmaceutical Science'
    PHYSCIENCE = 'Physical Science'
    VETMED = 'Veterinary Medicine'
    CHOOSE = ''
    FACULTIES = [
        ( AGRICULTURE,'Agricultural Science'),
        (  ARTS , 'Arts'),
        (  BIOLOGY, 'Biological Science'),
        (  MANAGEMENT ,'Management Science'),
        ( DENSITRY, 'Densitry'),
        ( EDUCATION ,'Education'),
        ( ENGNIEERING ,'Engineering'),
        ( HEANDTECH, 'Health Science and Technology'),
        ( LAW, 'Law'),
        ( MEDSCIENCE, 'Medical Science'),
        (  PHARM ,'Pharmaceutical Science'),
        ( PHYSCIENCE ,'Physical Science'),
        (  VETMED ,'Veterinary Medicine'),
        (CHOOSE, 'Choose A Faculty'),
    ]
    f_name = models.CharField(max_length=100,choices=FACULTIES, default=CHOOSE,verbose_name='Faculty')
    slug = models.SlugField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True,verbose_name='Description')

    def get_faculty_url(self):
        return reverse("faculty", args=[self.slug])




    def __str__(self) :
        if self.f_name is  None :
            return ''
        else:
            return self.f_name


    class Meta():
        verbose_name_plural = 'Faculties'



    # fac = mode