from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django_Pro",
            author="New_owner",
            price="200.00",
            genre="Programming"
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Django_Pro")
        self.assertEqual(f"{self.book.author}", "New_owner")
        self.assertEqual(f"{self.book.price}", "200.00")
        self.assertEqual(f"{self.book.genre}", "Programming")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django_Pro")
        self.assertTemplateUsed(response, "book/book_list.html")

    def test_book_detail_view(self):
        # Reverse the URL for the book_detail view
        url = reverse('book_detail', args=[str(self.book.id)])

        # Make a GET request to the URL
        response = self.client.get(url)
      #  response=self.client.get(self.book.reverse('book_detail'))
        no_response=self.client.get('/book_list/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "book/book_detail.html")


