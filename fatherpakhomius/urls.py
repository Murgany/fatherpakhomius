from django.urls import path
# successView #, audio_download,ContactView
from .views import category_list, sermon_list_by_category, book_list_by_category, PostView, IndexView, BookListView, SermonsView, LatestBookListView, OtherSermonsView, OtherBooksView, contactView, PostDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles', PostView.as_view(), name='articles'),
    path('articles/<int:pk>', PostDetailView.as_view(), name='articles'),

    path('sermons', SermonsView.as_view(), name='sermons'),
    path('other_sermons', OtherSermonsView.as_view(), name='other_sermons'),
    #   path('latest_sermons', LatestSermons.as_view(), name='latest_sermons'),

    path('book_list', BookListView.as_view(), name='book_list'),
    path('latest_books', LatestBookListView.as_view(), name='latest_books'),
    path('other_books', OtherBooksView.as_view(), name='other_books'),
    # path('book_categories', BookCategoryView.as_view(), name='book_categories'),
    # path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),

    # path('categories/', category_list, name='categories'),
    # path('sermon_categories/<int:pk>/', SermonCategoryDetailView.as_view(), name='sermon_category_detail'),
    # path('book_categories/<int:pk>/', BookCategoryDetailView.as_view(), name='book_category_detail'),

    path('categories/', category_list, name='category_list'),
    path('book-categories/<int:category_id>/books/', book_list_by_category, name='book_category_detail'),
    path('sermon-categories/<int:category_id>/sermons/', sermon_list_by_category, name='sermon_category_detail'),

    path('contact/', contactView, name='contact'),
    path('search_results', views.search_results, name='search-results'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
