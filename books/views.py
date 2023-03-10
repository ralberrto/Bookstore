from django.shortcuts import render
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"


class BookDetailView(generic.DeleteView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
