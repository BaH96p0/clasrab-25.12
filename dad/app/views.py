from datetime import date

from django.shortcuts import render
from .models import *
# Create your views here.



def index(request):
    # students = Student.objects.filter(course__name='PS')
    # courses = Student.objects.get(id=2).course.all()
    # python = Course.objects.get(name='PS')
    # student, _ = python.student_set.get_or_create(name='Bob')
    # # student = Student.objects.create(name='Tom')
    # st = Student.objects.get(id=3)
    # ps = Course.objects.get(name='PS')
    # ps.student_set.remove(st)
    # # res = Student.objects.get(id=3).course.all()
    # res = ps.student__set.all()

    # django = Course2.objects.get_or_create(name='Django')
    # tom = Student2.objects.get_or_create(name='Tom')
    # res, _ = Enrollment.objects.get_or_create(student=tom, course=django, date=date.today(), mark=5)
    # st = Student2.objects.get(id=2)
    # crs =Course2.objects.get(id=1)
    # res = st.course.all()
    # res = crs.student2_set.all()

    sam = Person.objects.get_or_create(name='akfaf')
    # res, _ = Account.objects.get_or_create(login='Krutoi', password=1234, user=sam)
    # res = Account.objects.get(user__id=3)
    # res.user.name='Samuel'
    # res.save()
    acc =Account(login='asfasdd', password='dewef')
    sam.acccount = acc
    sam.acccount.save()
    return render (request, 'app/index.html', context={'students':acc})