import json
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import UserMessageForm
from django.contrib import messages
from django.db.models import Q


# Global search function

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Search across all models using Q objects
        sermon_categories = SermonCategory.objects.filter(Q(name__icontains=query)) # | Q(description__icontains=query)
        book_categories = BookCategory.objects.filter(Q(name__icontains=query))  #| Q(description__icontains=query)
        sermons = Sermon.objects.filter(Q(title__icontains=query) | Q(speaker__icontains=query)| Q(description__icontains=query) | Q(category__name__icontains=query))
        other_sermons = SermonsByOtherFather.objects.filter(Q(title__icontains=query) | Q(speaker__icontains=query) | Q(description__icontains=query))
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) |Q(description__icontains=query) | Q(category__name__icontains=query))
        other_books = BooksByOtherFather.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query))
        chosen_sermons = ChosenSermon.objects.filter(Q(title__icontains=query) | Q(speaker__icontains=query) | Q(description__icontains=query)| Q(category__name__icontains=query))
        posts = Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)| Q(article__icontains=query))

        context = {
            'sermon_categories': sermon_categories,
            'book_categories': book_categories,
            'sermons': sermons,
            'other_sermons': other_sermons,
            'books': books,
            'other_books': other_books,
            'chosen_sermons': chosen_sermons,
            'posts': posts,
            'query': query,
        }
    else:
        context = {}
    return render(request, 'search_results.html', context)


# Posts list view

class PostView(ListView):
    model = Post
    template_name = "post.html"
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')
    paginate_by = 10


# Single Post view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# Category list view

def category_list(request):
    sermon_categories = SermonCategory.objects.all().order_by('-id')
    book_categories = BookCategory.objects.all().order_by('-id')
    context = {
        'sermon_categories': sermon_categories,
        'book_categories': book_categories,
    }
    return render(request, 'categories.html', context)


# Book list by category

def book_list_by_category(request, category_id):
    category = BookCategory.objects.get(pk=category_id)
    books = category.books.all().order_by('-id')
    other_books = category.other_books.all().order_by('-id')
    context = {
        'category': category,
        'books': books,
        'other_books': other_books
    }
    return render(request, 'book_category_detail.html', context)


# Sermons list by category
def sermon_list_by_category(request, category_id):
    category = SermonCategory.objects.get(pk=category_id)
    sermons_category = category.sermons.all().order_by('-id')
    other_sermons = category.other_sermons.all().order_by('-id')
    chosen_sermons = category.chosen_sermons.all().order_by('-id')
    context = {
        'category': category,
        'sermons_category': sermons_category,
        'other_sermons': other_sermons,
        'chosen_sermons': chosen_sermons,
    }
    return render(request, 'sermon_category_detail.html', context)


# Index view | home page

class IndexView(ListView):
    model = ChosenSermon
    template_name = 'index.html'
    context_object_name = 'chosen_sermons'
    queryset = ChosenSermon.objects.all().order_by('-id')
    # queryset = ChosenSermon.objects.prefetch_related('sermon_name').order_by('-id')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.last()
        return context


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


# Latest four books view | displayed in index.html page using Ajax
class LatestBookListView(ListView):
    model = Book
    template_name = "latest_books.html"
    context_object_name = 'latest_books'
    queryset = Book.objects.all().order_by('-id')
    paginate_by = 4


#  List of Sermons by other fathers view

class OtherSermonsView(ListView):
    model = SermonsByOtherFather
    template_name = "other_sermons.html"
    context_object_name = 'other_sermons'
    queryset = SermonsByOtherFather.objects.all().order_by('-id')
    paginate_by = 1


# List of books by other authors

class OtherBooksView(ListView):
    model = BooksByOtherFather
    template_name = "other_books.html"
    context_object_name = 'other_books'
    queryset = BooksByOtherFather.objects.all().order_by('-id')
    paginate_by = 1


# Contact view | render contact us page | Process form data
# Note: Form data is saved in database & viewable through admin site, not sent through SMTP.

def contact_view(request):
    if request.method == 'POST':
        contact_form = UserMessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, _('Your message was successfully sent!.'))
            return redirect('index')
        else:
            messages.error(request, _('Error sending message!.'))

    contact_form = UserMessageForm()
    return render(request=request, template_name='contact.html', context={'contact_form': contact_form})
