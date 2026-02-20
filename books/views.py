from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BooksForm

def book_list(request):
    books = Books.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("books:book_list")
    return render(request, "books/book_create.html", {"form": form})

def book_delete(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect("books:book_list")

def book_update(request, id):
    book = get_object_or_404(Books, id=id)
    form = BooksForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("books:book_list")

    return render(request, "books/book_update.html", {"form": form})







