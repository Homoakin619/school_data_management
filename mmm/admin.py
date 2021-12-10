from django.contrib import admin
from .models import Student,Result,Question,Sclass

admin.site.register(Student)
admin.site.register(Sclass)
admin.site.register(Result)
admin.site.register(Question)