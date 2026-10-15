
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Book_list, name='Book_list'),
    path('create/', views.Book_create, name='Book_create'),
    path('update/<int:id>/', views.Book_update, name='Book_update'),
    path('delete/<int:id>/', views.Book_delete, name='Book_delete'),
]