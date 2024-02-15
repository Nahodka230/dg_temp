from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book
from datetime import datetime
def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_date_view(request, pub_date):
    template = 'books/books_date_list.html'
    pub_date_res = datetime.strptime(pub_date, '%Y-%m-%d')
    books = Book.objects.filter(pub_date = pub_date_res)
    #books = Book.objects.all()
    #paginator = Paginator(books, 10)
    #page = paginator.get_page(pub_date_res)
    books_next = Book.objects.filter(pub_date__gt = pub_date_res).order_by('pub_date').first()
    if books_next:
        books_next = str(books_next.pub_date)
    else:
        books_next = None
    books_prev = Book.objects.filter(pub_date__lt = pub_date_res).order_by('pub_date').first()
    if books_prev:
        books_prev = str(books_prev.pub_date)
    else:
        books_prev = None
    context = {'books': books,
               'next_page': books_next,
               'previos_page':  books_prev,
               }

    return render(request, template, context)