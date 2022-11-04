from django.contrib import admin

from .models import Student, Teacher


class ConnectionsInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_filter = ['name']
    inlines = [ConnectionsInline]
    exclude = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_filter = ['name']
    inlines = [ConnectionsInline]
