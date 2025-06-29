from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    # Retrieve students ordered by student_number
    students = Student.objects.order_by('student_number')
    return render(request, 'students/index.html', {
        'students': students
    })

def view_student(request, id):
    student = Student.objects.get(pk = id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })
