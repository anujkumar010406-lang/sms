from django.urls import path
from . views import*

urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('logecode/',logcode,name='logcode'),
    path('news/',news,name='news'),
    


]