from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_list = Student.objects.order_by('group', 'name').prefetch_related('teachers')
    context = {'object_list': student_list}
    return render(request, template, context)
