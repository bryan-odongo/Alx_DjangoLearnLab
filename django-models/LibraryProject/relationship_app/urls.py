from django.urls import path
from .views import list_books
from .views import LibraryDetailView, add_book, edit_book, delete_book, register, user_login, user_logout
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", delete_book, name="delete_book"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]






# from django.urls import path
# from .views import add_book, edit_book, delete_book, register, user_login, user_logout
# from django.contrib.auth import views as auth_views

# urlpatterns = [
    
#     path("books/add/", add_book, name="add_book"),
#     path("books/edit/<int:book_id>/", edit_book, name="edit_book"),
#     path("books/delete/<int:book_id>/", delete_book, name="delete_book"),

#     path("register/", register, name="register"),
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
# ]

