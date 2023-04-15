from django.contrib import admin
from .models import Post, Sermon, SermonCategory, Book, BookCategory, BooksByOtherFather, SermonsByOtherFather, ChosenSermon, UserMessage


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email_address']
    readonly_fields = ['subject', 'email_address', 'message']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
class ChosenSermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'category', 'date_created']
    search_fields = ['title', 'speaker', 'audio', 'date_created']

class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'category', 'date_created']
    search_fields = ['title', 'speaker', 'audio', 'date_created']
    # fields = ['date_created']

class OtherSermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'category', 'date_created']
    search_fields = ['title', 'speaker', 'audio', 'speaker', 'date_created']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'date_created']
    search_fields = ['title', 'author', 'book', 'speaker', 'date_created']

class OtherBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'date_created']
    search_fields = ['title', 'author', 'book', 'speaker', 'date_created']


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created']
    search_fields = ['name', 'date_created']

class SermonCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created']
    search_fields = ['name', 'date_created']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']
    search_fields = ['name', 'author', 'date_created']


admin.site.register(ChosenSermon, ChosenSermonAdmin)
admin.site.register(Sermon, SermonAdmin)
admin.site.register(SermonCategory, SermonCategoryAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)

admin.site.register(BooksByOtherFather, OtherBookAdmin)
admin.site.register(SermonsByOtherFather, OtherSermonAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
