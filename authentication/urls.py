from django.urls import path
from . import views
from .views import upload_book, book_list, read_book

app_name = 'authentication'

urlpatterns = [
    path('', views.login_register_view, name='login_register'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),


    path('upload/', upload_book, name='upload_book'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', read_book, name='read_book'),  
]
