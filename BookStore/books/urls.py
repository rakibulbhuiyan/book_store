from django.urls import path
from books.views import BookListView, BookDetailView

urlpatterns = [
    path('book_list/', BookListView.as_view(), name='book_list'),
    path("book_list/<int:pk>/", BookDetailView.as_view(), name="book_detail"),

]
