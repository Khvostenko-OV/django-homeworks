from django.contrib import admin

# Register your models here.
from students.models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'birth_date', )


@admin.register(Course)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
