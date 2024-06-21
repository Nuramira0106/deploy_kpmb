from django.shortcuts import render
from Registrations.models import Course, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index (request):
    return render (request, "index.html")

def new_course (request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        find_data = Course.objects.filter(code=c_code).values()

        if find_data.count()==0:
            data=Course(code=c_code, description=c_desc)
            data.save()
            dict={
                'message':'Data save'
            }
        else:
            dict={
                'message':"Course" + find_data[0]['code']+"already exists"
            }
    else:
        dict={
            'message':''
        }
    return render (request,"new_course.html",dict)

def course (request):
    allcourse=Course.objects.all()
    dict={
        'allcourse': allcourse
    }
    return render (request, 'course.html', dict)

def search_course (request):
    if request.method == 'GET':
        data = Course.objects.filter(code = request.GET.get('c_code'))
        dict = {
                'data': data
            }
        return render (request, "search_course.html", dict)
    else:
        return render (request, 'search_course.html')

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request, "update_course.html", dict)

def save_update_course (request, code):
    c_desc = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data=Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

def student (request):
    data=0
    allstudent=Student.objects.all().values()
    if allstudent.count()!=0:
        data=1
        dict={
            'allstudent': allstudent,
            'data':data,
            }
    else:
        dict={
            'data':data,
        }
    return render (request, 'student.html', dict)

def new_student (request):
    allcourse=Course.objects.all().values()
    if request.method == 'POST':
        s_id = request.POST['id']
        s_name = request.POST['name']
        s_address = request.POST['address']
        s_phone = request.POST['phone']
        s_course = request.POST['c_course']
        find_data = Student.objects.filter(id=s_id).values()

        if find_data.count()==0:
            c_code=Course.objects.get(code=s_course)
            data=Student(id=s_id, name=s_name, address=s_address, phone=s_phone, course_code=c_code)
            data.save()
            dict={
                'allcourse':allcourse,
                'message':'Data save',
            }
        else:
            dict={
                'allcourse':allcourse,
                'message':"Student" + find_data[0]['id']+"already exists",
            
            }
    else:
        dict={
            'allcourse':allcourse,
            'message':'',
        }
    return render (request,"new_student.html",dict)

    