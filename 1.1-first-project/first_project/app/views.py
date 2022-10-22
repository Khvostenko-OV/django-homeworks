import datetime,os

#from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    time_str = str(current_time.time())
    return render(request, 'app/time.html', {'time': time_str.split('.')[0]})


def workdir_view(request):
    current_dir = os.listdir()
    return render(request, 'app/dir.html', {'dir_list': current_dir})
