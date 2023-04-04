from django.urls import path
from .views import IndexView, BookListView, SermonsView, LatestBookListView,OtherSermonsView, OtherBooksView, contactView, BookDetailView, LatestSermons # successView #, audio_download,ContactView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('sermons', SermonsView.as_view(), name='sermons'),
                  path('latest_books', LatestBookListView.as_view(), name='latest_books'),
                  path('book_list', BookListView.as_view(), name='book_list'),
                  path('contact/', contactView, name='contact'),
                  path('other_sermons', OtherSermonsView.as_view(), name='other_sermons'),
                  path('other_books', OtherBooksView.as_view(), name='other_books'),
                  path('latest_sermons', LatestSermons.as_view(), name='latest_sermons'),
                  # path('book_detail', BookDetailView.as_view(), name='book-detail'),
                  path('book-detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
                  path('search_results', views.search_results, name='search-results'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
