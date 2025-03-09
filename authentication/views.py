from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import Book
from .forms import BookUploadForm


def login_register_view(request):
    login_form = CustomLoginForm()
    register_form = CustomUserCreationForm()
    
    return render(request, 'authentication/login_register.html', {
        'login_form': login_form,
        'register_form': register_form,
    })

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('authentication:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    return redirect('authentication:login_register')

def register_view(request):
    login_form = CustomLoginForm()
    register_form = CustomUserCreationForm(request.POST or None)
    
    if request.method == 'POST':
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f"Registration successful. Welcome, {user.username}!")
            return redirect('authentication:dashboard')
        else:
            for field, errors in register_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            return render(request, 'authentication/login_register.html', {
                'login_form': login_form,
                'register_form': register_form,
                'register_error': True  # 👈 Add this flag
            })

    return redirect('authentication:login_register')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('authentication:login_register')

@login_required
def dashboard_view(request):
    return render(request, 'authentication/dashboard.html')

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('authentication:book_list')  # ✅ Use the namespace
    else:
        form = BookUploadForm()

    books = Book.objects.all()
    return render(request, 'books/upload_book.html', {'form': form, 'books': books})


from django.shortcuts import render, get_object_or_404
from django.db import models

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('authentication:book_list')  
    else:
        form = BookUploadForm(user=request.user)

    books = Book.objects.filter(user=request.user)  # Show only user's books
    return render(request, 'books/upload_book.html', {'form': form, 'books': books})


@login_required
def book_list(request):
    """Show only books that belong to the user or are public."""
    books = Book.objects.filter(models.Q(user=request.user) | models.Q(public=True))
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def read_book(request, book_id):
    """Ensure that users can only read their own books or public books."""
    book = get_object_or_404(Book, id=book_id)
    
    if not book.public and book.user != request.user:
        messages.error(request, "You do not have permission to view this book.")
        return redirect('authentication:book_list')

    return render(request, 'books/read_book.html', {'book': book})
