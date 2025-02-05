from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# from .models import Book
# -------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q
from django.http import HttpResponse

from django.contrib.auth.models import User
# print( User.objects.all() )  # Find an existing user

# Protect Book List with Login Required
@login_required
def book_list(request):
    query = request.GET.get('q', '')  # Get search term
    books = Book.objects.filter(bookstore_owner=request.user)  # Filter books by owner

    if query:
        books = books.filter(title__icontains=query)  # Apply search filter

    return render(request, 'books/list_books.html', {'books': books, 'query': query})

# Protect Book List with Login Required
@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        summary = request.POST.get('summary')

        if title and author:
            Book.objects.create(
                title=title,
                author=author,
                published_date=published_date if published_date else None,
                summary=summary,
                bookstore_owner=request.user  # Assign current user
            )
            return redirect('book_list')
        else:
            return HttpResponse("Title and Author are required fields!")

    return render(request, 'books/add_book.html')

# Protect Book List with Login Required
from django.shortcuts import get_object_or_404

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, bookstore_owner=request.user)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")

        published_date = request.POST.get("published_date")
        if published_date:  # ✅ Only update if not empty
            book.published_date = published_date
        else:
            book.published_date = None  # ✅ Allow clearing the date

        book.summary = request.POST.get("summary")
        book.save()
        return redirect("book_list")

    return render(request, "books/edit_book.html", {"book": book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, bookstore_owner=request.user)  # Ensure user owns the book
    book.delete()
    return redirect('book_list')


# --------------------------------------

# User Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'books/login.html', {'form': form})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
