from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv

station_list = []
with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        station_list.append({'Name': line['Name'], 'Street': line['Street'], 'District': line['District']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = request.GET.get('page', 1)
    paginator = Paginator(station_list, 10)
    page = paginator.get_page(page_number)
    stations_on_page = [s for s in page]
    context = {
         'bus_stations': stations_on_page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
