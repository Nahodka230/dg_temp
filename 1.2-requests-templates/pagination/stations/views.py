from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    list_bus_stations = []
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open (BUS_STATION_CSV, encoding = 'utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_bus_stations.append(row)
    page_number = int(request.GET.get("page",1))
    paginator = Paginator(list_bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations':  page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
