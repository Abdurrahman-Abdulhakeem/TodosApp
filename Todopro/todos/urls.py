from django.contrib import admin
from django.urls import path
from .views import todo_list_view, todo_detail_view, create_todo_view, delete_todo_view

urlpatterns = [
        path('list/', todo_list_view, name= 'list-todo'),
        path('list/detail/<int:id>/', todo_detail_view, name= 'detail-todo'),
        path('list/detail/<int:id>/delete/', delete_todo_view, name= 'delete-todo'),
        path('list/create/', create_todo_view, name='create-todo'),
]
