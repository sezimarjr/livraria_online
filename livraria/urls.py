from django.urls import path
from livraria import views

app_name = 'book'

urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    
    
    #BOOK
    path('book/<int:book_id>/',views.book, name='single_book'),
    
    #USER
    path('user/login/',views.login_view, name='login'),
]
