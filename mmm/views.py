from django.core.exceptions import ObjectDoesNotExist
from django.http import request
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import Class_Form, ResultsForm, SetQuestion, StudentForm,MyForm
from .models import Question, Student,Result,Sclass
from datetime import datetime
from django.template.defaultfilters import linebreaksbr
from django.core.paginator import Paginator

def home(request):
    context = {}
    return render(request,'home.html',context)


# List all registered Students
@login_required
def index(request):
    query = Student.objects.all()
    context = {'all':query,'page_title':'My School'}
    return render(request,'index.html',context)


# Register student in database
@login_required
def register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST or None,request.FILES)
        if form.is_valid(): 
            print('validform')
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else: 
        print('Form failed validation')
    context = {'form':form,'page_title':'Register Student'}
    return render(request,'register.html',context)


# Edit student details
@login_required
def edit(request,id):
    query = get_object_or_404(Student,id=id)
    sclass = Sclass.objects.get(student=query)
    print(sclass)
    form = StudentForm(instance=query)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form':form,'page_title':'Edit Student'}
    return render(request,'edit.html',context)

#  Here is the view for adding result to each student
@login_required
def add_result(request,id):
    query = get_object_or_404(Student,id=id)
    sclass = Sclass.objects.get(student=query)
    result = Result.objects.filter(student=query,student_class=sclass)
    x = len(result)
    if result:
        if x < 1:
            result = result[0]
        else:
            result = result[x - 1]
    form = ResultsForm()
    if request.method == 'POST':
        form = ResultsForm(request.POST)
        if form.is_valid():
            term1 = request.POST.get('term1')
            term2 = request.POST.get('term2')
            term3 = request.POST.get('term3')
            Result.objects.get_or_create(student=query,student_class=sclass,
                                                        term1=term1,term2=term2,term3=term3)
            return HttpResponseRedirect(reverse('index'))
    context = {'student':query,'form':form,'page_title':'Add Result'}
    return render(request,'add.html',context)

# Edit Result
@login_required
def edit_result(request,id):
    query = get_object_or_404(Student,id=id)
    student_class = Sclass.objects.get(student=query)
    result = Result.objects.get(student=query,student_class=student_class)
    form = ResultsForm(instance=result)
    if request.method == 'POST':
        form = ResultsForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'id':id}))
    context = {'form':form,'page_title':'Edit Result'}
    return render(request,'edit_result.html',context)

@login_required
def school_fee(request,id):
    query = get_object_or_404(Student,id=id)
    student_class = Sclass.objects.get(student=query)
    form = Class_Form(instance=student_class)
    if request.method == 'POST':
        form = Class_Form(request.POST,instance=student_class)
        if form.is_valid():
            print('valid Form')
            form.save()
            return HttpResponseRedirect(reverse('detail',kwargs={'id':id}))
        else:print('Validation form Failed')
    context = {'student':query,'form':form,'class':student_class,'page_title':'Edit Fee'}
    return render(request,'school_fee.html',context)

@login_required
def search(request):
    if request.method == 'POST':
        to_search = request.POST.get('search')
        firstname = Student.objects.filter(firstname__icontains=to_search)
        lastname = Student.objects.filter(lastname__icontains=to_search)
        klass = Student.objects.filter(present_class__icontains=to_search)
        if firstname:
            context = {'result':firstname}
            return render(request,'search_results.html',context)
        elif lastname:
            context = {'result':lastname}
            return render(request,'search_results.html',context)
        elif klass:
            context = {'result':klass}
            return render(request,'search_results.html',context)
        else:
            all_students = Student.objects.all()
            context = {'all':all_students,'search_failed':'There is no matching result for the search query'}
            return render(request,'failed_search.html',context)
    return redirect('index')

# Student Detail
@login_required
def detail(request,id):
    query = get_object_or_404(Student,id=id)
    sclass = Sclass.objects.get(student=query)
    result = Result.objects.filter(student=query,student_class=sclass)
    check = False
    if sclass.outstanding == 0:
        check = True
    x = len(result)
    if result:
        if x < 1:
            result = result[0]
        else:
            result = result[x - 1]
    print(result)
    context ={'student':query,'class':sclass,'result':result,'page_title':'Detail','check':check}
    return render(request,'detail.html',context)

# List of Senior Students
@login_required
def senior_students(request):
    que = Student.objects.filter(present_class__startswith='S')
    query = que[:]
    print(query)
    context = {'query':query,'page_title':'Senior Students'}
    return render(request,'senior.html',context)

# Test Interface
def interface(request):
    all_questions = Question.objects.all()
    questions = []
    for que in all_questions:
        questions.append(que)

    pass_count = 0
    fail_count = 0
    
    paginator = Paginator(all_questions,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total = len(questions)
    if request.method == 'POST':
        for question in all_questions:
            print(request.POST.get(question.question))
            ans = request.POST.get('option')
            print(question.answer)
            print(ans)
            if ans:
                if ans == question.answer :
                    pass_count += 1
                else:
                    fail_count += 1
            else:
                error = 'Kindly select an answer!'
                context = {'questions':all_questions,'error':error}
                return render(request,'interface.html',context)


    context = {'questions':all_questions,'index':index,'total':total,'page_obj':page_obj}
    return render(request,'interface.html',context)

# List of junior Students
@login_required
def junior_students(request):
    que = Student.objects.filter(present_class__startswith='J')
    query = que[:]
    print(query)
    context = {'query':query,'page_title':'Junior Students'}
    return render(request,'junior.html',context)

# Exam Center home
def exam_home(request):
    context = {}
    return render(request,'exam.html',context)

# Test Registration Page
def start(request):
    name = request.POST.get('name')
    if request.method == 'POST':
        if name:
            return HttpResponseRedirect(reverse('interface'))
        else:
            error = 'Please enter your name!'
            context = {'error':error}
            return render(request,'start_exam.html',context)
    context = {}
    return render(request,'start_exam.html',context)

# Page for setting Questions and Answers
def set_question(request):
    form = SetQuestion()
    if request.method == 'POST':
        form = SetQuestion(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success'))
    context = {'form':form}
    return render(request,'set_question.html',context)

# Successful Setting of Question
def success(request):
    context = {}
    return render(request,'success.html',context)

def jss1(request):
    context = {'page_title':'Jss1'}
    return render(request,'js1.html',context)

def jss2(request):
    context = {'page_title':'Jss2'}
    return render(request,'js2.html',context)

def jss3(request):
    context = {'page_title':'Jss3'}
    return render(request,'js3.html',context)

def sss1(request):
    context = {'page_title':'Sss1'}
    return render(request,'ss1.html',context)

def sss2(request):
    context = {'page_title':'Sss2'}
    return render(request,'ss2.html',context)

def sss3(request):
    context = {'page_title':'Sss3'}
    return render(request,'ss3.html',context)

