from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateList
from .models import ToDoList

# Create your views here.

def index(response):
    return render(response, 'main/base.html')

def home(response):
    return render(response, 'main/home.html')

def create(response):

    if response.method == 'POST':
        form = CreateList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()

    else:
        form = CreateList()
    return render(response, 'main/create.html', {"form":form})