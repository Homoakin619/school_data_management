# Generated by Django 3.2.4 on 2021-08-13 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True)),
                ('date_of_admission', models.DateField(blank=True)),
                ('class_of_admission', models.CharField(blank=True, choices=[('J1', 'JSS 1'), ('J2', 'JSS 2'), ('J3', 'JSS 3'), ('S1', 'SSS 1'), ('S2', 'SSS 2'), ('S3', 'SSS 3'), ('G', 'Graduated')], max_length=2)),
                ('present_class', models.CharField(blank=True, choices=[('J1', 'JSS 1'), ('J2', 'JSS 2'), ('J3', 'JSS 3'), ('S1', 'SSS 1'), ('S2', 'SSS 2'), ('S3', 'SSS 3'), ('G', 'Graduated')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_class', models.CharField(blank=True, choices=[('J1', 'JSS 1'), ('J2', 'JSS 2'), ('J3', 'JSS 3'), ('S1', 'SSS 1'), ('S2', 'SSS 2'), ('S3', 'SSS 3'), ('G', 'Graduated')], max_length=2)),
                ('school_fee', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('outstanding', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmm.student')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term1', models.TextField(blank=True, null=True)),
                ('term2', models.TextField(blank=True, null=True)),
                ('term3', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmm.student')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmm.sclass')),
            ],
        ),
    ]
