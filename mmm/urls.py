from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (add_result, detail, edit, edit_result, exam_home, home,index, interface, jss1, jss2, jss3,register, school_fee, 
                    senior_students,junior_students, set_question, sss1, sss2, sss3, start, success,search)

urlpatterns = [
    path('',home,name='home'),
    path('index/',index,name='index'),
    path('register/',register,name='register'),
    path('search/',search,name='search'),
    path('add/<int:id>/',add_result,name='add'),
    path('edit/<int:id>/',edit,name='edit'),
    path('edit_result/<int:id>/',edit_result,name='edit_result'),
    path('school_fee/<int:id>/',school_fee,name='school_fee'),
    path('detail/<int:id>/',detail,name='detail'),
    path('senior/',senior_students,name='senior'),
    path('junior/',junior_students,name='junior'),
    path('set_questions/',set_question,name='set-question'),
    path('success/',success,name='success'),
    
    
    path('exam_home/',exam_home,name='exam'),
    path('exam/start/',start,name='start'),
    path('exam/interface/',interface,name='interface'),

    path('exam/j1/',jss1,name='j1'),
    path('exam/j2/',jss2,name='j2'),
    path('exam/j3/',jss3,name='j3'),
    path('exam/s1/',sss1,name='s1'),
    path('exam/s2/',sss2,name='s2'),
    path('exam/s3/',sss3,name='s3'),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)