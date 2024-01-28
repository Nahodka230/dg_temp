from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', '')
    #     phones = phones.order_by(sort_by)
    if sort_by:
        match sort_by:
            case 'name':
                phones = Phone.objects.order_by('name')
            case 'min_price':
                phones = Phone.objects.order_by('price')
            case 'max_price':
                phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {"phone": phone}
    return render(request, template, context)
