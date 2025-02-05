from django.urls import path
# from .views import register_view, login_view, logout_view, book_list
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_list/', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
