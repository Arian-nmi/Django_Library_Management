from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from books.forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, id_):
    book = get_object_or_404(Book, id=id_)
    return render(request, 'book_detail.html', {'book': book})


def book_create_update(request, id_=None):
    if id_:
        book = get_object_or_404(Book, id=id_)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})
