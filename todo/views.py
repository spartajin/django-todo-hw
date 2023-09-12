from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Todo
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        print(todos)
        context = {
            "todos":todos,
        }
        return render(request, "todo/index.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)


@csrf_exempt
def create(request):
    if request.method == "POST":
        print(request.POST["content"])
        Todo.objects.create(content=request.POST["content"])
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("Invalid request method", status=405)
    
def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        "todo": todo,
    }
    return render(request, "todo/detail.html")

@csrf_exempt
def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect("/todo/")
    else:
        return HttpResponse("Invalid request method", status=405)
    

@csrf_exempt
def update(request, todo_id):
    if request.method == "POST":
        # have to make update
        return redirect("/todo/")
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo": todo,

        }
        return render(request, "todo/update.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)