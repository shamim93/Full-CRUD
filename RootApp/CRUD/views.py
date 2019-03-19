from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from CRUD.models import BookList
from CRUD.forms import BookForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/')

    else:
        form = BookForm()
    return render(request, 'CRUD/index.html', {'form': form})

def home(request):
    books = BookList.objects.all()
    return render(request, 'CRUD/home.html',{'books':books})

def edit(request,id):
    book = BookList.objects.get(pk=id)
    return render(request,'CRUD/edit.html', {'book':book})

def update(request,id):
    book = BookList.objects.get(pk=id)
    form = BookForm(request.POST,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'CRUD/edit.html',{'book':book})
def remove(request,id):
    book = BookList.objects.get(pk=id)
    book.delete()

    return redirect('/')



