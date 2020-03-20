from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views

# import notifications

urlpatterns = [
	path('home/', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),		

	# books module
	path('books/', include(('books.urls', 'books'), namespace='books')),
	# bookrequests module
	path('requests/', include(('bookrequests.urls', 'requests'), namespace='requests')),
	# notifications
    # url('^inbox/notifications/', include(notifications.urls)),
]
