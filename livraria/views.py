from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from livraria.models import Book
from django.core.paginator import Paginator

# Create your views here.


def index(request):
  books = Book.objects.all().order_by('-id')[:150]
  print(books[0].category.filter()[:1])
  
  context = {
    'books':books,
    
  }
  
  return render(request, 'livraria/index.html',context)

def book(request,book_id):
  print(book_id)
  single_book = get_object_or_404(
    Book,
    pk=book_id,
  )
  
  context = {
    'single_book':single_book,
  }
  
  return render(request, 'livraria/book.html',context)