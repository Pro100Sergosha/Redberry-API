from django.db import models

class GeneralInfo(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
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


class Resume(models.Model):
    general = models.ManyToManyField(GeneralInfo)
    experience = models.ManyToManyField(ExperienceInfo)
    education = models.ManyToManyField(EducationInfo)
    photo = models.ImageField(null=True)