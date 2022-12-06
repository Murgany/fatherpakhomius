from datetime import date
from django.views.generic import ListView
from .models import Sermon, Book, SermonCategory, BookCategory, Litergie, SermonsByOtherFathers, BooksByOtherFathers
import os
import mimetypes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
# from .forms import RenewBookForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.generic.edit import FormView


# home page view
class IndexView(ListView):
    model = Sermon
    template_name = 'index.html'
    context_object_name = 'sermons'
    # queryset = Sermon.objects.filter(make_published=True, ).order_by('-id')
    queryset = Sermon.objects.all().order_by('-id')
    paginate_by = 1

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     books = Book.objects.all().order_by('-id')
    #     # sermon_categories = SermonCategory.objects.all()
    #     context["books"] = books
    #     # context2 ['books', 'books', ] = all_sermons
    #     return context


# All sermons list view
class SermonsView(ListView):
    model = Sermon
    template_name = "sermons.html"
    context_object_name = 'sermons_list'
    queryset = Sermon.objects.all().order_by('-id')
    paginate_by = 2


# All books list view
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = 'book_list'
    queryset = Book.objects.all().order_by('-id')
    paginate_by = 4


# Latest three books view to be displayed in home page (index) by the help of Jquery
class LatestBookListView(ListView):
    model = Book
    template_name = "latest_books.html"
    context_object_name = 'latest_books'
    queryset = Book.objects.all().order_by('-id')
    paginate_by = 4


class Liturgies(ListView):
    model = Litergie
    template_name = "liturgies.html"
    context_object_name = 'liturgies'
    queryset = Litergie.objects.all().order_by('-id')


#  List of Sermons by other fathers view
class OtherSermonsView(ListView):
    model = SermonsByOtherFathers
    template_name = "other_sermons.html"
    context_object_name = 'other_sermons'
    queryset = SermonsByOtherFathers.objects.all().order_by('-id')
    paginate_by = 2

class OtherBooksView(ListView):
    model = BooksByOtherFathers
    template_name = "other_books.html"
    context_object_name = 'other_books'
    queryset = BooksByOtherFathers.objects.all().order_by('-id')
    paginate_by = 2


from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import HttpResponse, HttpResponseRedirect

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            email_address = form.cleaned_data["email_address"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email_address, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("index")
    return render(request, "contact.html", {"form": form})

