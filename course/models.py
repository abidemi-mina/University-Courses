from django.db import models
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
    name = models.CharField(max_length=100, null=True,blank=True)
    job = models.TextField(null=True,blank=True)

    def __str__(self) :
        return self.name

    class Meta():
        verbose_name_plural = 'Departments'


class Faculty(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    depts = models.ManyToManyField(Department)




    def __str__(self) :
        if self.name is  None :
            return ''
        else:
            return self.name

    class Meta():
        verbose_name_plural = 'Faculties'



    # fac = mode