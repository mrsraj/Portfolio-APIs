from django.db import models

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
    fk_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='skills_details')

class SkillsDetails(models.Model):
    relatedskills = models.TextField()
    fk_Skills = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='skills_details')
    
class Suggestion(models.Model):
    message = models.TextField()