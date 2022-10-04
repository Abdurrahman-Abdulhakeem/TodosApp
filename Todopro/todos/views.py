from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodo

# Create your views here.

def todo_list_view(request):
    todo_list = Todo.objects.all()

    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/todo_list.html', context)

def todo_detail_view(request, id):
    todo_detail = Todo.objects.get(id=id)

    context = {
        'todo_detail': todo_detail
    }
    return render(request, 'todos/todo_detail.html', context)

def create_todo_view(request):
    form = CreateTodo()
    if request.method == 'POST':
        form = CreateTodo(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todo.objects.create(**form.cleaned_data)
            return redirect('../')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'todos/todo_create.html', context)

def delete_todo_view(request, id  ):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('../../../')

    context = {
        'todo': todo
    }
    return render(request, 'todos/todo_delete.html', context)




