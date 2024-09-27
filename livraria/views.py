from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from livraria.models import Book
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.


def index(request):
  books = Book.objects.all().order_by('-id')
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


def search(request):
  
  search_value = request.GET.get('q','').strip()
  if not search_value:
    return redirect('book:index')
  select_filter = request.GET.get('selected_filter')
  
  
  
  
  if search_value:
    if select_filter == 'title':
      filter_books = Book.objects.filter(
        title__icontains=search_value
      )
    elif select_filter == 'author':
      filter_books = Book.objects.filter(
        author__name__icontains=search_value
      )
    elif select_filter == 'category':
      filter_books = Book.objects.filter(
        category__name__icontains=search_value
      )
  
  context = {
    'books':filter_books,
  }
  
  return render(request, 'livraria/index.html',context)


def login_view(request):
  form = AuthenticationForm(request)
  if request.user.is_authenticated:
    return redirect('book:index')
  
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    
    if form.is_valid():
      user = form.get_user()
      auth.login(request, user)
      return redirect('book:index')
    
  return render(request, 'livraria/login.html',{'form':form})