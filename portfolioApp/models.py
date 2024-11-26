from django.db import models
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    name = models.CharField(max_length=200)

    
class StudentDetails(models.Model):
    universityname = models.CharField(max_length=50)
    collegename = models.CharField(max_length=300)
    branch = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    passion = models.CharField(max_length=200)  # Added max_length
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='details')


class Experience(models.Model):
    companyname = models.CharField(max_length=250)
    companyaddr = models.CharField(max_length=250)
    position = models.CharField(max_length=200)
    projectdescription = models.TextField()
    usedskills = models.CharField(max_length=500)
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='experience_details')

class Skills(models.Model):
    skills = models.CharField(max_length=150)  # Corrected max_length
    skills_logo = models.CharField(max_length=500, default='null')
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='skills_details')

class SkillsDetails(models.Model):
    relatedskills = models.TextField()
    fk_Skills = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='skills_details')
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=1000)
    usedSkills = models.CharField(max_length=200)
    
    
class Suggestion(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.TextField(max_length=100, default=None)
    message = models.TextField()
    date = models.DateTimeField(_("Date"), auto_now_add=True)