from django.urls import path
from livraria import views

app_name = 'book'

urlpatterns = [
    path('',views.index, name='index'),
    
    
    #BOOK CRUD
    path('book/<int:book_id>/',views.book, name='single_book'),
]
