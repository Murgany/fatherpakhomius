from django.contrib import admin
from .models import Sermon, SermonCategory, Book, BookCategory, Litergie, BooksByOtherFathers, SermonsByOtherFathers


admin.site.register(Sermon)
admin.site.register(SermonCategory)

admin.site.register(Book)
admin.site.register(BookCategory)

admin.site.register(Litergie)
admin.site.register(BooksByOtherFathers)
admin.site.register(SermonsByOtherFathers)



