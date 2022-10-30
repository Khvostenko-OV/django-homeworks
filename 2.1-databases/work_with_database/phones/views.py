from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_mode = request.GET.get('sort', 'id')
    phone_list = Phone.objects.order_by(sort_mode)
    template = 'catalog.html'
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=slug)
    context = {'phone': product}
    return render(request, template, context)
