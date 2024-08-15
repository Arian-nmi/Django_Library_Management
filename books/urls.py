from django.urls import path
from books.views import book_list, book_detail, book_create_update

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('book/new/', book_create_update, name='book_create_update'),
    path('book/edit/<int:id>/', book_create_update, name='book_edit'),
]
