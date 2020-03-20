from django.urls import path, include

from books import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add_book/', views.add_book, name='add_book'),
	path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
	path('delete/<int:id>/', views.delete, name='delete'),
	path('search/', views.search, name='search'),
	path('make_request/<int:id>/', views.make_request, name='make_request'),
]