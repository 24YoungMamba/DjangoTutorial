from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    subject = models.CharField(max_length=128, unique=True)

    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name="classes")

    def __str__(self):
        return self.subject


class Test(models.Model):
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

    title = models.CharField(max_length=52)
    guide_lines = models.FileField(upload_to="guide_lines/")

    def __str__(self):
        return self.title


class WorkSheet(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    
    test = models.ForeignKey(Test, related_name="student_worksheets", on_delete=models.CASCADE)
    sheet = models.FileField(upload_to="worksheets/")

    def __str__(self):
        return f"Worksheet, by {self.student.username}"


class Grade(models.Model):
    CHOICES = [
        ("F", 0),
        ("D", 60),
        ("C", 70),
        ("B", 80),
        ("A", 100),
    ]

    worksheet = models.ForeignKey(WorkSheet, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=CHOICES, default=CHOICES[0])

    def __str__(self):
        return str(self.grade)