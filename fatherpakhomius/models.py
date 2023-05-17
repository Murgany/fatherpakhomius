from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class SermonCategory(models.Model):
    """
    This model represents a sermon category. It has the following fields:

    name: The name of the category.
    date_created: The date the category was created.
    """
    name = models.CharField(_('sermon category name'), max_length=200)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)
   
    class Meta:
        verbose_name = _('Sermon Category')
        verbose_name_plural = _('Sermon Categories')
    
    def get_absolute_url(self):
        """Returns the url to access a particular sermon category"""
        return reverse('sermon_category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    """
    This model represents a book category. It has the following fields:

    name: The name of the category.
    date_created: The date the category was created.
    """
    name = models.CharField(_('book category name'), max_length=200)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _('Book Category')
        verbose_name_plural = _('Book Categories')
    
    def get_absolute_url(self):
        """Returns the url to access a particular book category"""
        return reverse('book_category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Sermon(models.Model):
    """
    This model represents a sermon. It has the following fields:

    title: The title of the sermon.
    speaker: The name of the speaker.
    category: The category of the sermon.
    audio: The audio file for the sermon.
    video: The video file for the sermon.
    description: A description of the sermon.
    date_created: The date the sermon was created.
    """
    title = models.CharField(_('sermon title'), max_length=200)
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    category = models.ForeignKey(SermonCategory, related_name='sermons', verbose_name=_('sermon category'), on_delete=models.CASCADE, default="")
    audio = models.FileField(_("sermon audio"), upload_to='audio')
    video = models.FileField(_("video"), upload_to='video', blank=True)
    description = models.TextField(_("description"), max_length=1000, blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)
    
    class Meta:
        verbose_name = _('Sermon')
        verbose_name_plural = _('Sermons')

    def get_absolute_url(self):
        """Returns the url to access a particular sermon instance."""
        return reverse('sermon_category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class SermonsByOtherFather(models.Model):
    """
    This model represents a sermon by another father. It has the following fields:

    title: The title of the sermon.
    speaker: The name of the speaker.
    category: The category of the sermon.
    audio: The audio file for the sermon.
    video: The video file for the sermon.
    description: A description of the sermon.
    external_link: An external link to the sermon.
    date_created: The date the sermon was created.
    """
    title = models.CharField(_("sermon title"), max_length=200)
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    category = models.ForeignKey(SermonCategory, related_name='other_sermons', verbose_name=_("sermon category"), on_delete=models.CASCADE, default="")
    audio = models.FileField(_("sermon audio"), upload_to='audio', blank=True, )
    video = models.FileField(_("video"), upload_to='video', blank=True, )
    description = models.TextField(_("description"), max_length=1000, blank=True)
    external_link = models.URLField(_("external link"), max_length=200, blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _('Sermons by other father')
        verbose_name_plural = _('Sermons by other fathers')

    def display_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    def __str__(self):
        return self.title


class Book(models.Model):
    """
    This model represents a book. It has the following fields:

    title: The title of the book.
    author: The name of the author.
    category: The category of the book.
    book: The file for the book.
    image: The cover image for the book.
    description: A description of the book.
    date_created: The date the book was created.
    """
    title = models.CharField(_('book title'), max_length=200)
    author = models.CharField(_('author'), max_length=100, blank=True)
    category = models.ForeignKey(BookCategory,related_name='books', verbose_name=_('book category'), on_delete=models.CASCADE, default="")
    book = models.FileField(_('book instance'), upload_to='books', )
    image = models.ImageField(_('image'), upload_to='images', blank=True, )
    description = models.TextField(_('description'), max_length=1000, blank=True, )
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title


class BooksByOtherFather(models.Model):
    """
    This model represents a book by another father. It has the following fields:

    title: The title of the book.
    author: The name of the author.
    category: The category of the book.
    book: The file for the book.
    image: The cover image for the book.
    description: A description of the book.
    external_link: An external link to the book.
    date_created: The date the book was created.
    """
    title = models.CharField(_('book title'), max_length=200)
    author = models.CharField(_('author'), max_length=200, blank=True, )
    category = models.ForeignKey(BookCategory, related_name='other_books', verbose_name=_('book category'), on_delete=models.CASCADE, default="")
    book = models.FileField(_('book instance'), upload_to='books', )
    image = models.ImageField(_('image'), upload_to='images', blank=True, )
    description = models.TextField(_('description'), max_length=1000, blank=True, )
    external_link = models.URLField(_('external link'), max_length=200, blank=True, )
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _('Book by another father')
        verbose_name_plural = _('Books by other fathers')

    def __str__(self):
        return self.title


class ChosenSermon(models.Model):
    """
    This model represents a chosen sermon. It has the following fields:

    title: The title of the sermon.
    speaker: The name of the speaker.
    category: The category of the sermon.
    description: A description of the sermon.
    audio: The audio file for the sermon.
    date_created: The date the sermon was created.
    """
    title = models.CharField(_('title'), max_length=200, default='')
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    category = models.ForeignKey(SermonCategory, related_name='chosen_sermons', verbose_name=_('sermon category'), on_delete=models.CASCADE, default="")
    description = models.TextField(_('description'), max_length=1000, blank=True, )
    audio = models.FileField(_("sermon audio"), upload_to='audio', blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _('Chosen Sermon')
        verbose_name_plural = _('Chosen Sermons')

    def __str__(self):
        return f'{self.title}'
    

class UserMessage(models.Model):
    """
    This model represents a message sent by a user. It has the following fields:

    subject: The subject of the message.
    email_address: The email address of the sender.
    message: The message itself.
    date_created: The date the message was created.
    """
    subject = models.CharField(_('subject'), max_length=100)
    email_address = models.EmailField(_('email_address'), max_length=80)
    message = models.CharField(_('message'), max_length=1000)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)

    class Meta:
        verbose_name = _("User Message")
        verbose_name_plural = _("User Messages")

    # returns a human-readable string (subject)
    def __str__(self):
        return self.subject


class Post(models.Model):
    """
    This model represents a post (an article). It has the following fields:

    title: The title of the post.
    author: The author of the post article.
    article: The article (the post itself).
    image: The image for the post.
    date_created: The date the post was created.
    """
    title = models.CharField(_("title"), max_length=100)
    author = models.CharField(_('author'), max_length=100, blank=True)
    article = models.TextField(_("article"), max_length=5000)
    image = models.FileField(_('image'), upload_to='images', blank=True)
    date_created = models.DateTimeField(_('date_created'), auto_now=False, editable=True)
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def get_absolute_url(self):
        """Returns the url to access a particular post."""
        return reverse('articles', args=[str(self.id)])

    # returns a human-readable title
    def __str__(self):
        return self.title
    
