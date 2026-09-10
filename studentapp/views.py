from django.shortcuts import render
from adminapp.models import Student
from adminapp.models import Attendance
from teacherapp.models import StudyMaterial
# Create your views here.
def studenthome(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid) 
            return render(req,'studenthome.html',{'studentid':studentid,'student':student})

    except KeyError:
        return redirect('login')


def stuattend(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            att=Attendance.objects.filter(sid=student.id)
            return render(req,'stuattend.html',{'studentid':studentid,'student':student,'att':att})

    except KeyError:
        return redirect('login')

def stuslm(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            slm=StudyMaterial.objects.filter(tclass=student.sclass) 
            return render(req,'stuslm.html',{'studentid':studentid,'student':student,'slm':slm})

    except KeyError:
        return redirect('login')

