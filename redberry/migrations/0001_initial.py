# Generated by Django 5.0.6 on 2024-06-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=100)),
                ('degree', models.CharField(choices=[('საშუალო სკოლის დიპლომი', 'საშუალო სკოლის დიპლომი'), ('ზოგადსაგანმანათლებლო დიპლომი', 'ზოგადსაგანმანათლებლო დიპლომი'), ('ბაკალავრი', 'ბაკალავრი'), ('მაგისტრი', 'მაგისტრი'), ('დოქტორი', 'დოქტორი'), ('ასოცირებული ხარისხი', 'ასოცირებული ხარისხი'), ('სტუდენტი', 'სტუდენტი'), ('კოლეჯი', 'კოლეჯი'), ('სხვა', 'სხვა')], max_length=28)),
                ('end_date', models.DateField()),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('employer', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=17)),
            ],
        ),
    ]
