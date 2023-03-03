from django.shortcuts import render
from .models import *
from .forms import BookForm
# Create your views here.
def index(request):
    context = {
        'books' : Book.objects.all(),
        'category' : Category.objects.all(),
        'form' : BookForm(),
    }
    return render(request,'pages/index.html',context)

def books(request):    
    context = {
        'books' : Book.objects.all(),
        'category' : Category.objects.all()
    }
    return render(request,'pages/books.html',context)

def delete(request):
    return render(request,'pages/delete.html')

def update(request):
    return render(request,'pages/update.html')

