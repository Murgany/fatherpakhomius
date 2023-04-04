import json
from django.views.generic import ListView
from .models import Sermon, Book, SermonCategory, BookCategory, SermonsByOtherFathers, BooksByOtherFathers
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _
from django.utils import translation

from django.views import generic


# language = 'ar'
# translation.activate(language)

# home page view

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books = Book.objects.filter(description__icontains=searched, title__icontains=searched)
        sermons = Sermon.objects.filter(description__icontains=searched, title__icontains=searched)
        other_sermons = SermonsByOtherFathers.objects.filter(description__icontains=searched, title__icontains=searched)
        other_books = BooksByOtherFathers.objects.filter(description__icontains=searched, title__icontains=searched)

        context = {
            'searched': searched,
            'sermons': sermons,
            'other_sermons': other_sermons,
            'books': books,
            'other_books': other_books,
        }
        return render(request, "search_results.html", context)


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class IndexView(ListView):
    model = Sermon
    template_name = 'index.html'
    context_object_name = 'sermons'
    queryset = Sermon.objects.all().order_by('-id')
    paginate_by = 1


class LatestSermons(ListView):
    model = Sermon
    template_name = 'latest_sermons.html'
    context_object_name = 'latest_sermons'
    queryset = Sermon.objects.all().order_by('-id')
    paginate_by = 5
    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    # context['qs_to_json'] = json.dumps(list(Sermon.objects.values()))
    # # context['qs_to_json'] = Sermon.objects.values()
    # return context


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


#  List of Sermons by other fathers view
class OtherSermonsView(ListView):
    model = SermonsByOtherFathers
    template_name = "other_sermons.html"
    context_object_name = 'other_sermons'
    queryset = SermonsByOtherFathers.objects.all().order_by('-id')
    paginate_by = 1


class OtherBooksView(ListView):
    model = BooksByOtherFathers
    template_name = "other_books.html"
    context_object_name = 'other_books'
    queryset = BooksByOtherFathers.objects.all().order_by('-id')
    paginate_by = 1


from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import HttpResponse, HttpResponseRedirect


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data[_("subject")]
            email_address = form.cleaned_data[_("email_address")]
            message = form.cleaned_data[_('message')]
            try:
                send_mail(subject, message, email_address, ["fathepakhomius@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("index")
    return render(request, "contact.html", {"form": form})
