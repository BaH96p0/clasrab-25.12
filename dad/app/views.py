from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from .forms import *
# Create your views here.

class BookCreateView(CreateView):
    model = Author
    fields = ('name, author')
    template_name = 'app/index.html'
    context_object_name = 'authors'
    success_url = '/classes/'

class BookUpdateView(UpdateView):
    model = Book
    fields = ('name, author')
    template_name = 'app/index.html'
    context_object_name = 'authors'
    success_url = '/classes/'


class ArticleView(ListView):
    model = Author
    template_name = 'app/info.html'

def index(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'app/index.html',context={'form':BookForm()})

def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'app/author.html',context={'form':AuthorForm()})

def update_book(request, id):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('author')
    return render(request, 'app/updateBook.html',context={'form':BookForm(instance=book)})


class BookView(View):
    def get(self, request, **args, **kwargs):
        return render(request, 'app/index.html', context={'form':BookForm(), 'authors': Author.objects.all()})
    def post(self, request, **args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')



