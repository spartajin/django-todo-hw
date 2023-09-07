from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo


# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    return HttpResponse("create")