from django.shortcuts import render
from models import Book
def book_list(request):
    listado = Book.objects.all()
    context = {"context": listado}
    return render(request, "/core/book_list.html", context)
