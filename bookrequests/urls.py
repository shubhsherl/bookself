from django.urls import path, include

from bookrequests import views

urlpatterns = [
	path('lent/', views.lent_index, name='lent'),
	path('borrowed/', views.borrowed_index, name='borrowed'),
	# path('accept/(?P<id>\d+)/$', views.accept, name='accept'),
	# path('reject/(?P<id>\d+)/$', views.reject, name='reject'),
	# path('return/(?P<id>\d+)/$', views.return_book, name='return'),
]
