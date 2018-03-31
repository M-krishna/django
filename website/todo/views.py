from django.shortcuts import render, redirect
from .forms import TodoApp
from .models import Todo
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoApp()
    context = {'mytodo': mytodo, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addNewTodo(request):
    form = TodoApp(request.POST)
    
    if form.is_valid():
        my_new_todo = Todo(text=request.POST['text'])
        my_new_todo.save()
    
    return redirect('index')

def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()

    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def resetTodo(request):
    Todo.objects.all().delete()
    return redirect('index')