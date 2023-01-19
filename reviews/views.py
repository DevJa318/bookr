from django.shortcuts import render, get_object_or_404

from .models import Book, Review
from .utils import average_rating


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            numbers_of_reviews = len(reviews)
        else:
            book_rating = None
            numbers_of_reviews = 0
        book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': numbers_of_reviews})
        context = {'book_list': book_list}
    return render(request, 'reviews/book_list.html', context)

def book_info(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {'book':book,'book_rating': book_rating, 'reviews': reviews}
    else:
        context = {'book':book,'book_rating': None, 'reviews': None }
    return render(request, "reviews/book_info.html", context)