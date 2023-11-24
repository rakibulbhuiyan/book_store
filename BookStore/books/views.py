from django.shortcuts import render
from django.views import generic
from books.models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = "book/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = "books"
    template_name = "book/book_detail.html"
