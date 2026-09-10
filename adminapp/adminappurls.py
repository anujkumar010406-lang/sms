from django.urls import path
from.import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('addclass/',views.addclass,name='addclass'),
    path('viewclass/',views.viewclass,name='viewclass'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('viewsubject/',views.viewsubject,name='viewsubject'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('editclass/<id>',views.editclass,name='editclass'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('viewteacher/',views.viewteacher,name='viewteacher'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('addnoti/',views.addnoti,name='addnoti'),
    path('viewnoti/',views.viewnoti,name='viewnoti'),

    
   
]