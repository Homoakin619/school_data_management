from django.db.models import fields
from mmm.models import Result, Sclass, Student,Question
from django import forms


CLASS_CHOICES = (
    ('J1','JSS1'),
    ('J2','JSS2'),
    ('J3','JSS3'),
    ('S1','SSS1'),
    ('S2','SSS2'),
    ('S3','SSS3')
)

SEX_CHOICES = (
    ('M','Male'),
    ('F','Female')
)

class StudentForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'form-control form-control-sm',
                                    'placeholder':'Enter your firstname'
                                }
                                ))
    lastname = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'form-control form-control-sm',
                                    'placeholder':'Enter your lastname'
                                }
                                ))
    sex = forms.ChoiceField(choices=SEX_CHOICES,widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control form-control-sm'}))
    date_of_admission = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control form-control-sm'}))
    class_of_admission = forms.ChoiceField(choices=CLASS_CHOICES,widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    present_class = forms.ChoiceField(choices=CLASS_CHOICES,widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control-file col-md-6','type':'file'}))
    class Meta:
        model = Student
        fields = ['firstname','lastname','sex','date_of_birth',
                  'date_of_admission','class_of_admission','present_class','image']


class Class_Form(forms.ModelForm):
    present_class = forms.ChoiceField(choices=CLASS_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    school_fee = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    paid = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    outstanding = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Sclass
        fields = ('present_class','school_fee','paid','outstanding')

class MyForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter your firstname'
                                }
                                ))
    lastname = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter your lastname'
                                }
                                ))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control col-md-6','type':'file'}))
    class Meta:
        model = Student
        fields = ('firstname','lastname','image')

class ResultsForm(forms.ModelForm):
    term1 = forms.Textarea()
    term2 = forms.Textarea()
    term3 = forms.Textarea()
    class Meta:
        model = Result
        fields = ('term1','term2','term3')

# Set Question and Answer Form
class SetQuestion(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea(attrs={
                                'class':'form-control',
    }))
    answer = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
    }))
    option1 = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
    }))
    option2 = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
    }))
    option3 = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
    }))
    option4 = forms.CharField(widget=forms.TextInput(attrs={
                                'class':'form-control',
    }))
    
    class Meta:
        model = Question
        fields = ['question','answer','option1','option2','option3','option4']
    