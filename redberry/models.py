from django.db import models

class GeneralInfo(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    bio = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=17)

class ExperienceInfo(models.Model):
    position = models.CharField(max_length=100)
    employer = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    info = models.TextField()

class EducationInfo(models.Model):
    DEGREE_CHOICES = (
        ('საშუალო სკოლის დიპლომი', 'საშუალო სკოლის დიპლომი'),
        ('ზოგადსაგანმანათლებლო დიპლომი','ზოგადსაგანმანათლებლო დიპლომი'),
        ('ბაკალავრი','ბაკალავრი'),
        ('მაგისტრი','მაგისტრი'),
        ('დოქტორი','დოქტორი'),
        ('ასოცირებული ხარისხი','ასოცირებული ხარისხი'),
        ('სტუდენტი','სტუდენტი'),
        ('კოლეჯი','კოლეჯი'),
        ('სხვა','სხვა'),
    )
    education = models.CharField(max_length=100)
    degree = models.CharField(max_length=28, choices=DEGREE_CHOICES)
    end_date = models.DateField()
    info = models.TextField()