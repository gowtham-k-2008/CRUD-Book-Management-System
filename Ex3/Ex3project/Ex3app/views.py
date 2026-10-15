from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def Book_list(request):
    Books = Book.objects.all()
    return render(request, 'Book_list.html',
                  {'Books': Books})

def Book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('Book_list')

    return render(request, 'Book_form.html')

def Book_update(request, id):
    Book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        Book.title = request.POST.get('title')
        Book.author = request.POST.get('author')
        Book.price = request.POST.get('price')
        student.save()

        return redirect('Book_list')

    return render(request, 'Book_form.html',
                  {'Book': Book})

def Book_delete(request, id):
    Book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        Book.delete()

    return redirect('Book_list')
