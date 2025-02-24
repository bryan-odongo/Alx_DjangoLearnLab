from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import permission_required, user_passes_test
from .forms import BookForm

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to home after signup
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# View to Add a Book (Restricted)
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form})

# View to Edit a Book (Restricted)
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form})

# View to Delete a Book (Restricted)
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# -----------------------------
# Task 3: Role-Based Access Control Views
# -----------------------------

def is_admin(user):
    return user.is_authenticated and \
           hasattr(user, 'userprofile') and \
           user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and \
           hasattr(user, 'userprofile') and \
           user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and \
           hasattr(user, 'userprofile') and \
           user.userprofile.role == "Member"

# # Helper function to check if the user is an Admin
# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

# @user_passes_test(is_admin)
# def admin_view(request):
#     # Render a template that displays Admin-specific content.
#     return render(request, "relationship_app/admin_view.html")

# # Helper function to check if the user is a Librarian
# def is_librarian(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     # Render a template that displays Librarian-specific content.
#     return render(request, "relationship_app/librarian_view.html")

# # Helper function to check if the user is a Member
# def is_member(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# @user_passes_test(is_member)
# def member_view(request):
#     # Render a template that displays Member-specific content.
#     return render(request, "relationship_app/member_view.html")






# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic.detail import DetailView  # Required import for DetailView
# from .models import Book, Library
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.decorators import permission_required, user_passes_test
# # Import BookForm if defined in forms.py (or define it if needed)
# from .forms import BookForm  # Ensure this is defined in your projec

# # User Registration View
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("home")  # Redirect to home after signup
#     else:
#         form = UserCreationForm()
#     return render(request, "relationship_app/register.html", {"form": form})

# # User Login View
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("home")  # Redirect to home after login
#     else:
#         form = AuthenticationForm()
#     return render(request, "relationship_app/login.html", {"form": form})

# # User Logout View
# def user_logout(request):
#     logout(request)
#     return render(request, "relationship_app/logout.html")
# # View to Add a Book (Restricted)
# @permission_required("relationship_app.can_add_book", raise_exception=True)
# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("list_books")
#     else:
#         form = BookForm()
#     return render(request, "relationship_app/book_form.html", {"form": form})

# # View to Edit a Book (Restricted)
# @permission_required("relationship_app.can_change_book", raise_exception=True)
# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect("list_books")
#     else:
#         form = BookForm(instance=book)
#     return render(request, "relationship_app/book_form.html", {"form": form})

# # View to Delete a Book (Restricted)
# @permission_required("relationship_app.can_delete_book", raise_exception=True)
# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == "POST":
#         book.delete()
#         return redirect("list_books")
#     return render(request, "relationship_app/book_confirm_delete.html", {"book": book})


# # Function-Based View: List all books
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# # Class-Based View: Display library details
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "relationship_app/library_detail.html"  # Updated path
#     context_object_name = "library"
    


# # -----------------------------
# # Role-Based Access Control Views
# # -----------------------------
# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

# @user_passes_test(is_admin)
# def admin_view(request):
#     # Render a template that displays Admin-specific content.
#     return render(request, "relationship_app/admin_view.html")

# def is_librarian(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     # Render a template that displays Librarian-specific content.
#     return render(request, "relationship_app/librarian_view.html")

# def is_member(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# @user_passes_test(is_member)
# def member_view(request):
#     # Render a template that displays Member-specific content.
#     return render(request, "relationship_app/member_view.html")




