from django.db import models

SEX_CHOICES = (
    ('M','Male'),
    ('F','Female')
)

CLASS_CHOICES = (
    ('J1','JSS 1'),
    ('J2','JSS 2'),
    ('J3','JSS 3'),
    ('S1','SSS 1'),
    ('S2','SSS 2'),
    ('S3','SSS 3'),
    ('G','Graduated')
)

class Student(models.Model):
    image = models.ImageField(blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX_CHOICES,max_length=1,blank=True)
    date_of_birth = models.DateField(blank=True)
    date_of_admission = models.DateField(blank=True)
    class_of_admission = models.CharField(choices=CLASS_CHOICES,max_length=2,blank=True)
    present_class = models.CharField(choices=CLASS_CHOICES,max_length=2,blank=True)

    def save(self, **kwargs):
        if self.pk is None:
            super(Student, self).save(**kwargs)
            paid = 0
            if self.present_class == 'J1':
                school_fee = 25000
            elif self.present_class == 'J2':
                school_fee = 30000
            elif self.present_class == 'J3':
                school_fee = 35000
            elif self.present_class == 'S1':
                school_fee = 40000
            elif self.present_class == 'S2':
                school_fee = 45000
            else:
                school_fee = 50000
            outstanding = school_fee - paid
            
            klass = Sclass(student=self,present_class=self.present_class,
                            school_fee=school_fee,outstanding=outstanding,paid=paid)
            klass.save()
            result = Result(student=self,student_class=klass)
            result.save()
     
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
	

class Sclass(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    present_class = models.CharField(choices=CLASS_CHOICES,max_length=2,blank=True)
    school_fee = models.IntegerField()
    paid = models.IntegerField()
    outstanding = models.IntegerField()

    def save(self,*args,**kwargs):
        if self.pk is None:
            if self.school_fee:
                self.outstanding = 0
                self.outstanding = self.school_fee - self.paid
                super(Sclass,self).save(**kwargs)
        else:
            self.outstanding = self.school_fee - self.paid
            super(Sclass,self).save(**kwargs)

    def __str__(self):
        return '%s %s : %s' %(self.student.firstname,self.student.lastname,self.present_class)

    def get_present_class(self):
        if self.student.present_class:
            rclass = self.student.present_class
            self.present_class = rclass
        else:
            self.present_class = 'No class'
        return self.present_class

    def get_school_fee(self):
        return self.school_fee

    def get_outstanding(self):
        self.outstanding = self.school_fee - self.paid
        return self.outstanding
	
		
class Result(models.Model):
    student_class = models.ForeignKey(Sclass,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    term1 = models.TextField(blank=True)
    term2 = models.TextField(blank=True)
    term3 = models.TextField(blank=True)

    def __str__(self):
        return f'Result {self.id}'


class Question(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.question
