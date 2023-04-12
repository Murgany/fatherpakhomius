from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class SermonCategory(models.Model):
    name = models.CharField(_('sermon category name'), max_length=200)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)

    
    class Meta:
        verbose_name = _('Sermon Category')
        verbose_name_plural = _('Sermon Categories')
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(_('book category name'), max_length=200)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)

    
    class Meta:
        verbose_name = _('Book Category')
        verbose_name_plural = _('Book Categories')
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Sermon(models.Model):
    title = models.CharField(_('sermon title'), max_length=200)
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    category = models.ForeignKey(SermonCategory, verbose_name=_('sermon category'), on_delete=models.CASCADE, default="")
    audio = models.FileField(_("sermon audio"), upload_to='audio', blank=True)
    video = models.FileField(_("video"), upload_to='video', blank=True)
    description = models.TextField(_("description"), max_length=1000, blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)
    
    class Meta:
        verbose_name = _('Sermon')
        verbose_name_plural = _('Sermons')

    def display_category(self):
        """Creates a string for the category. This is required to display aategory in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('sermon-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class SermonsByOtherFather(models.Model):
    title = models.CharField(_("sermon title"), max_length=200)
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    author = models.CharField(_("author"), max_length=200, blank=True, )
    category = models.ForeignKey(SermonCategory, verbose_name=_("sermon category"), on_delete=models.CASCADE, default="")
    audio = models.FileField(_("sermon audio"), upload_to='audio', blank=True, )
    video = models.FileField(_("video"), upload_to='video', blank=True, )
    # image = models.ImageField(_("image"), upload_to='images', blank=True, )
    description = models.TextField(_("description"), max_length=1000, blank=True)
    external_link = models.URLField(_("external link"), max_length=200, blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)

    
    class Meta:
        verbose_name = _('Sermons by other father')
        verbose_name_plural = _('Sermons by other fathers')

    def display_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('sermon-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(_('book title'), max_length=200)
    author = models.CharField(_('author'), max_length=100, blank=True)
    category = models.ForeignKey(BookCategory, verbose_name=_('book category'), on_delete=models.CASCADE, default="")
    book = models.FileField(_('book instance'), upload_to='books', )
    image = models.ImageField(_('image'), upload_to='images', blank=True, )
    description = models.TextField(_('description'), max_length=1000, blank=True, )
    date_created = models.DateTimeField(_("date_created"), auto_now=True)


    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('book-detail', args=[str(self.id)])


class BooksByOtherFather(models.Model):
    title = models.CharField(_('book title'), max_length=200)
    author = models.CharField(_('author'), max_length=200, blank=True, )
    category = models.ForeignKey(BookCategory, verbose_name=_('book category'), on_delete=models.CASCADE, default="")
    book = models.FileField(_('book instance'), upload_to='books', )
    image = models.ImageField(_('image'), upload_to='images', blank=True, )
    description = models.TextField(_('description'), max_length=1000, blank=True, )
    external_link = models.URLField(_('external link'), max_length=200, blank=True, )
    date_created = models.DateTimeField(_("date_created"), auto_now=True)

    
    class Meta:
        verbose_name = _('Book by another father')
        verbose_name_plural = _('Books by other fathers')

    def display_category(self):
        """Creates a string for the Category. This is required to display category in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])

    display_category.short_description = 'Category'

    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('other-books-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class ChosenSermon(models.Model):
    # sermon_name = models.ForeignKey(Sermon, verbose_name=_('sermon name'), on_delete=models.CASCADE, default='', related_name='chosen')
    sermon_name = models.CharField(_('sermon name'), max_length=200)
    speaker = models.CharField(_('speaker'), max_length=100, blank=True)
    category = models.ForeignKey(SermonCategory, verbose_name=_('sermon category'), on_delete=models.CASCADE, default="")
    audio = models.FileField(_("sermon audio"), upload_to='audio', blank=True)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)

    
    class Meta:
        verbose_name = _('Chosen Sermon')
        verbose_name_plural = _('Chosen Sermons')

    def __str__(self):
        return f'{self.sermon_name}'
    

class UserMessage(models.Model):
    subject = models.CharField(_('subject'), max_length=100)
    email_address = models.EmailField(_('email_address'), max_length=80)
    message = models.CharField(_('message'), max_length=1000)
    date_created = models.DateTimeField(_("date_created"), auto_now=True)


    class Meta:
        verbose_name = _("User Message")
        verbose_name_plural = _("User Messages")

    def __str__(self):
        return self.subject
