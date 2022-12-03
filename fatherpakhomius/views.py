from datetime import date
from django.views.generic import ListView
from .models import Sermon, Book, SermonCategory, BookCategory, Litergie
import os
import mimetypes
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect
# from .models import Book, BookInstance, Genre, Author
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
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


# class BookDetailView(generic.DetailView):
#     model = Book

    # def pdf_view(request):
    #     with open('E:\mypdf.pdf', 'rb') as pdf:
    #         response = HttpResponse(pdf.read(), content_type='application/pdf')
    #         response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
    #         return response

#
# def audio_download(request, pk):
#     download = get_object_or_404(Sermon, pk=pk)
#     file = download.audio.audio.url.strip('/')
#     wrapper = FileWrapper(open(file, 'rb'))
#     response = HttpResponse(wrapper, content_type='application/force-download')
#     response['Content-Disposition'] = "attachment; filename=" + os.path.basename(file)
#     print('response')
#     return response
#
#
# import os
# from django.conf import settings
# from django.http import HttpResponse, Http404
#
# def downloads(request):
#     context = {'files': Sermon.objects.all()}
#     return render(request, 'downloads.html', context)
#
# def download_file(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type='application/admin_upload')
#             response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
#             return response
#     raise Http404


# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = 'index.html'
#
#     def form_valid(self, form):
#         form.send_mail()
#         return super().form_valid(form)


# class ContactView(FormView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, *args, **kwargs):
#        context = super(ContactView, self).get_context_data(*args, **kwargs)
#        context['form'] = ContactForm()
#        return context


from django.core.mail import send_mail, BadHeaderError

# class ContactView(FormView):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         send_mail(self, form.cleaned_data, )
#         return super(ContactView, self).form_valid(form)
#
#     def send_mail(self, valid_data):
#         # Send mail logic
#         print(valid_data)
#         pass

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


# def successView(request):
#     return HttpResponse("Success! Thank you for your message.")

# def index(request):
#     num_books = Book.objects.all().count
#     num_instances = BookInstance.objects.all().count()
#     num_instances_available = BookInstance.objects.filter(status='a').count()  # status_exact='a'
#     num_authors = Author.objects.count()
#     genres = Genre.objects.all()

    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1
    # context = {
    #     'num_books': num_books,
    #     'num_instances': num_instances,
    #     'num_instances_available': num_instances_available,
    #     'num_authors': num_authors,
    #     'genres': genres,
    #     'num_visits': num_visits,
    # }
    # return render(request, 'index.html', context)

# class AuthorListView(generic.ListView):
#     model = Author
#     paginate_by = 10

# class AuthorDetailView(generic.DetailView):
#     model = Author

# class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
#     model = BookInstance
#     template_name = 'locallibrary/user_borrowed_books.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back')
#
#
# class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
#     model = BookInstance
#     permission_required = 'locallibrary.can_mark_returned'
#     template_name = 'locallibrary/all_borrowed_books.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return BookInstance.objects.filter(status='o').order_by('due_back')


# @login_required
# @permission_required('locsllibrsry.can_mark_returned', raise_exception=True)
# def renew_book_librarian(request, pk):
#     book_instance = get_object_or_404(BookInstance, pk=pk)
#
#     if request.method == 'POST':
#         form = RenewBookForm(request.POST)
#         if form.is_valid():
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()
#             return HttpResponseRedirect(reverse('all-borrowed'))
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
#
#     context = {'form': form, 'book_instance': book_instance}
#     return render(request, 'book_renew_librarian.html', context)


# from .models import FilesAdmin


# def login(request):
#     return render(request, 'login.html')

