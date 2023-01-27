from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_info, name='book-info'),
    path('book-search/', views.book_search, name='book_search'),
]