from django.urls import path
from .views import IndexView, BookListView, SermonsView, LatestBookListView, Liturgies, contactView # successView #, audio_download,ContactView
# from django import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('sermons', SermonsView.as_view(), name='sermons'),
                  path('latest_books', LatestBookListView.as_view(), name='latest_books'),
                  path('book_list', BookListView.as_view(), name='book_list'),
                  path('liturgies', Liturgies.as_view(), name='liturgies'),
                  # path('contact/', ContactView.as_view(), name='contact'),
                  path('contact/', contactView, name='contact'),

                  # path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
                  # path('audio_download/<int:pk>', audio_download, name='audio_download'),
                  # path("success", successView, name="success"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import  tkinter

# import turtle
# wn = turtle.Screen()
# june = turtle.Turtle()
#
# for _ in range(20):
#     june.color("green", "yellow")
#     june.forward(50)
#     june.right(90 + 2)
#     june.forward(50 + 5)
#     june.right(90 + 5)
