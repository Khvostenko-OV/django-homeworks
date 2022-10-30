from django.shortcuts import render, redirect

from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    sort_mode = request.GET.get('sort', 'id')
    book_list = Book.objects.order_by(sort_mode)
    context = {'books': book_list, 'date_before': '', 'date_after': ''}
    return render(request, template, context)

def books_by_date(request, show_date):
    template = 'books/books_list.html'
    sort_mode = request.GET.get('sort', 'id')
    book_list = Book.objects.filter(pub_date=show_date).order_by(sort_mode)
    book_before = Book.objects.filter(pub_date__lt=show_date).order_by('-pub_date')
    if book_before:
        date_before = str(book_before[0].pub_date)
    else:
        date_before = ''
    book_after = Book.objects.filter(pub_date__gt=show_date).order_by('pub_date')
    if book_after:
        date_after = str(book_after[0].pub_date)
    else:
        date_after = ''
    context = {'books': book_list, 'date_before': date_before, 'date_after': date_after}
    return render(request, template, context)
